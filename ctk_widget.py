import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


class CTkMeter(ttk.Label):
    """
        A custom Tkinter widget that displays a circular progress meter.

        :param parent: The parent widget.
        :type parent: tkinter.Widget
        :param hover_effect: Whether to enable the hover effect. Defaults to False.
        :type hover_effect: bool
        :param refresh_animation: Whether to refresh the animation when the value is set. Defaults to False.
        :type refresh_animation: bool
        :param kwargs: Additional keyword arguments to pass to the ttk.Label initializer.
        """
    def __init__(self, parent, hover_effect=False, refresh_animation=False, command=None, **kwargs):
        """
                Initialize the CTkMeter widget.

                :param parent: The parent widget.
                :type parent: tkinter.Widget
                :param hover_effect: Whether to enable the hover effect animation. Defaults to False.
                :type hover_effect: bool
                :param refresh_animation: Whether to refresh the animation when the value is set. Defaults to False.
                :type refresh_animation: bool
                :param command: Passes 'on-click' command.
                :param kwargs: Additional keyword arguments to pass to the ttk.Label initializer.
                """
        self.arc = None
        self.im = Image.new('RGBA', (1000, 1000))
        self.min_value = kwargs.get('minvalue') or 0
        self.max_value = kwargs.get('maxvalue') or 100
        self.size = kwargs.get('size') or 200
        self.font = kwargs.get('font') or 'Calibri 14 bold'
        self.background = kwargs.get('background')
        self.foreground = kwargs.get('foreground') or '#777'
        self.troughcolor = kwargs.get('troughcolor') or '#003547'
        self.indicatorcolor = kwargs.get('indicatorcolor') or '#11608f'
        self.arcvariable = tk.IntVar(value='text')
        self.arcvariable.trace_add('write', self.update_arcvariable)
        self.textvariable = tk.StringVar()
        self.hover_effect = hover_effect
        self.refresh_animation = refresh_animation
        self.command = command
        self.setup()
        kwargs.pop('troughcolor', None)
        kwargs.pop('indicatorcolor', None)

        super().__init__(parent, image=self.arc, compound='center', style='Gauge.TLabel',
                         textvariable=self.textvariable, **kwargs)
        # Bind the <Enter> event to the loading_hover_effect method

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)



    def on_enter(self, event):
        if self.command:
            self.configure(cursor="hand2")
        self.loading_hover_effect(None)

    def on_leave(self, event):
        self.configure(cursor="")

    def on_click(self, event):
        if self.command:
            self.command()

    def setup(self):
        """Setup routine"""
        style = ttk.Style()
        style.configure('Gauge.TLabel', font=self.font, foreground=self.foreground)
        if self.background:
            style.configure('Gauge.TLabel', background=self.background)
        draw = ImageDraw.Draw(self.im)
        draw.arc((0, 0, 990, 990), 0, 360, self.troughcolor, 100)
        self.arc = ImageTk.PhotoImage(self.im.resize((self.size, self.size), Image.LANCZOS))

    def update_arcvariable(self, *args):
        """Redraw the arc image based on variable settings"""
        angle = int(float(self.arcvariable.get())) + 90
        self.im = Image.new('RGBA', (1000, 1000))
        draw = ImageDraw.Draw(self.im)
        draw.arc((0, 0, 990, 990), 0, 360, self.troughcolor, 100)
        draw.arc((0, 0, 990, 990), 90, angle, self.indicatorcolor, 100)
        self.arc = ImageTk.PhotoImage(self.im.resize((self.size, self.size), Image.LANCZOS))
        self.configure(image=self.arc)

    def loading_hover_effect(self, event):
        if self.hover_effect and isinstance(self, CTkMeter):
            actual_val = self.arcvariable.get()  # 360 maximum
            if actual_val <= 360:
                self.arcvariable.set(actual_val - 15)
                updated_val = self.arcvariable.get()
                for i in range(1, 16):
                    self.arcvariable.set(updated_val + i)
                    self.after(5, self.update_idletasks())

    def set(self, value):
        """Set the value of arcvariable and call loading_hover_effect if refresh_value is True"""
        self.arcvariable.set(value)
        if self.refresh_animation:
            self.loading_hover_effect(None)
