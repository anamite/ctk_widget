# ctk_widget

ctk_widget is a python file consisting of new and modern widgets for customtkinter library.

## Installation

Download and move the ctk_widget.py file in the same folder as your python environment

Install required Dependencies:

- [Pillow](https://pillow.readthedocs.io/en/latest/installation.html)


# Usage
Currently Available Widgets:
- CTkMeter

## CTkMeter
```python
from ctk_widget import CTkMeter


#---- add this code inside your root frame

card = ct.CTkFrame(root, height=296, width=240, fg_color='#76aaea', corner_radius=8)
card.grid_propagate(False)
card.grid(row=1, column=i, padx=8, pady=8)
meter = CTkMeter(card, refresh_animation=True, hover_effect=True, padding=19, background='#76aaea',
                foreground=accent_col_3, troughcolor='#f7e2c8',
                indicatorcolor='#eab676')
meter.grid(row=0, column=0, pady=3) 

meter.set(200) # Value must be between 0 and 360

meter.textvariable.set(f'{int(((gauge.arcvariable.get())/360)*100)}%') # To set the text in the middle

label = ct.CTkLabel(card, text='Progress', text_color='#ffffff',
                      font=('Calibri Bold', 22))
label.grid(row=1, column=0)


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
