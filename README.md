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
A cool and Modern looking Meter widget with hover animation for CustomTkinter Library.

![image](https://github.com/anamite/ctk_widget/assets/77412636/d53b3537-45a5-4b05-8d21-a70e61a09b45)





**New Attributes** :
| Parameters |Description |
| --- | --- |
| background | Background Color |
|  troughcolor | Trough Color of Meter |
|  indicatorcolor | Indicator Color of Meter |
| foreground | Sets the text color |
|  hover_effect | Shows an animation when hovered, set to *False* by default |
|  refresh_animation | Loading animation when increased or reduced value, set to *False* by default |
| command | To pass required on click command to the Meter widget |


**Example Code** :
```python
import customtkinter as ct
from ctk_widget import CTkMeter

root = ct.CTk()
ct.set_appearance_mode("White")
root.minsize(height=500, width=550)
root.configure(bg_color='#fafafa')


# Function for testing command
def clicked():
    label_1.configure(text='Clicked!')


# Creating a Card Frame to display the meter widget
card1 = ct.CTkFrame(root, height=365, width=240, fg_color='#ffffff', corner_radius=8)
card1.grid_propagate(False)
card1.grid(row=0, column=0, padx=15, pady=15, rowspan=3)
meter = CTkMeter(card1, refresh_animation=True, hover_effect=True, padding=19, background='#ffffff',
                 foreground='#000000', troughcolor='#b6b6de', font='Calibri 14 bold',
                 indicatorcolor='#0f1273', command=clicked)
meter.grid(row=0, column=0, pady=5)

meter.set(214)  # Value must be between 0 and 360

meter.textvariable.set(f'{int((meter.arcvariable.get() / 360) * 100)}%')  # To set the text

# Labeling the Meter
label_1 = ct.CTkLabel(card1, text='Progress', text_color='#0f1273',
                      font=('Calibri Bold', 32))
label_1.grid(row=1, column=0, pady=20)

# ------------------Card2 on right


card2 = ct.CTkFrame(root, height=100, width=260, fg_color='#ffffff', corner_radius=8)
card2.grid_propagate(False)
card2.grid(row=0, column=1, padx=5, pady=0)
meter_2 = CTkMeter(card2, refresh_animation=True, hover_effect=True, padding=19, background='#ffffff',
                   foreground='#000000', troughcolor='#b6b6de', font='Calibri 12 bold',
                   indicatorcolor='#31a36b', command=clicked, size=60)
meter_2.grid(row=0, column=0, pady=0, padx=8, sticky='nsew')
meter_2.set(120)  # Value must be between 0 and 360

meter_2.textvariable.set(f'{int((meter_2.arcvariable.get() / 360) * 100)}%')  # To set the text

# Labeling the meter_2
label = ct.CTkLabel(card2, text='Progress', text_color='#0f1273',
                    font=('Calibri Bold', 22))
label.grid(row=0, column=1, sticky='nsew')

# ------------------Card3 on right


card3 = ct.CTkFrame(root, height=100, width=260, fg_color='#ffffff', corner_radius=8)
card3.grid_propagate(False)
card3.grid(row=1, column=1, padx=5, pady=0)
meter_3 = CTkMeter(card3, refresh_animation=True, hover_effect=True, padding=19, background='#ffffff',
                   foreground='#000000', troughcolor='#b6b6de', font='Calibri 12 bold',
                   indicatorcolor='#3887bc', command=clicked, size=60)
meter_3.grid(row=0, column=0, pady=0, padx=8, sticky='nsew')
meter_3.set(40)  # Value must be between 0 and 360

meter_3.textvariable.set(f'{int((meter_3.arcvariable.get() / 360) * 100)}%')  # To set the text

# Labeling the meter_3
label = ct.CTkLabel(card3, text='Progress', text_color='#0f1273',
                    font=('Calibri Bold', 22))
label.grid(row=0, column=1, sticky='nsew')

# ------------------Card4 on right


card4 = ct.CTkFrame(root, height=100, width=260, fg_color='#ffffff', corner_radius=8)
card4.grid_propagate(False)
card4.grid(row=2, column=1, padx=5, pady=0)
meter_4 = CTkMeter(card4, refresh_animation=True, hover_effect=True, padding=19, background='#ffffff',
                   foreground='#000000', troughcolor='#b6b6de', font='Calibri 12 bold',
                   indicatorcolor='#279b67', command=clicked, size=60)
meter_4.grid(row=0, column=0, pady=0, padx=8, sticky='nsew')
meter_4.set(320)  # Value must be between 0 and 360

meter_4.textvariable.set(f'{int((meter_4.arcvariable.get() / 360) * 100)}%')  # To set the text

# Labeling the meter_4
label = ct.CTkLabel(card4, text='Progress', text_color='#0f1273',
                    font=('Calibri Bold', 22))
label.grid(row=0, column=1, sticky='nsew')

# ------------------------Card for slider
card5 = ct.CTkFrame(root, height=30, width=260, fg_color='#ffffff', corner_radius=8)
card5.grid_propagate(False)
card5.grid(row=3, column=0, columnspan=2, padx=5, pady=20)

slider = ct.CTkSlider(card5, from_=0, to=360, number_of_steps=100, width=245, command=lambda value: meter.set(value))
slider.grid(row=0, column=0, padx=8, pady=8)

root.mainloop()

```

**Other Methods:**
- .set() : To set the meter to a specific value. (NOTE: value must be between 0 and 360)
- .arcvariable.get() : To get the current value in the meter
- .textvariable.set('String') : To set the text inside the meter


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
