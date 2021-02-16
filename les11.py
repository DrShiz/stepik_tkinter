from tkinter import *

window = Tk()

scale = Scale(window)
scale.config(from_=10, to=500, orient=HORIZONTAL)
spinbox = Spinbox(window)
spinbox.config(values=('One', 'Two', 'Three'))
scale.pack()
spinbox.pack()

window.mainloop()
