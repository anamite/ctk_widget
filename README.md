# ctk_widget

ctk_widget is a python file consisting of new and modern widgets for customtkinter library.

## Installation

Download and move the ctk_widget.py file in the same folder as your python environment

**Install required Dependencies:**

- [Pillow](https://pillow.readthedocs.io/en/latest/installation.html)


# Usage
Currently Available Widgets:
- CTkMeter

## CTkMeter
![image](https://github.com/anamite/ctk_widget/assets/77412636/d52ec4e3-8141-40dc-9ed4-11e45061fc9e)

I took and modified this code from the meter widget of ttkbootstrap library.
Works fine inside customtkinter

New Attributes:
| Parameters |Description |
| --- | --- |
| background | Background Color |
|  troughcolor | Trough Color of Meter |
|  indicatorcolor | Indicator Color of Meter |
|  hover_effect | Shows an animation when hovered, set to *False* by default |
|  refresh_animation | Loading animation when increased or reduced value, set to *False* by default |


```python
import customtkinter as ct
from ctk_widget import CTkMeter

root = ct.CTk()
ct.set_appearance_mode("White")
root.minsize(height=400, width=600)
root.configure(bg_color = '#fafafa')

# Creating a Card Frame to display the meter widget
card = ct.CTkFrame(root, height=300, width=240, fg_color='#ffffff', corner_radius=8)
card.grid_propagate(False)
card.grid(row=0, column=0, padx=80, pady=80)
meter = CTkMeter(card, refresh_animation=True, hover_effect=True, padding=19, background='#ffffff',
                 foreground='#000000', troughcolor='#b6b6de',
                 indicatorcolor='#0f1273')
meter.grid(row=0, column=0, pady=5)

meter.set(97)  # Value must be between 0 and 360

meter.textvariable.set(f'{int((97 / 360) * 100)}%')  # To set the text

# Labeling the Meter
label = ct.CTkLabel(card, text='Progress', text_color='#0f1273',
                    font=('Calibri Bold', 22))
label.grid(row=1, column=0)


root.mainloop()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
