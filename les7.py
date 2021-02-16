from tkinter import *

counter = 0


def increase_value(event):
    global counter
    counter = counter + 1
    text1.config(text=str(counter))


def decrease_value(event):
    global counter
    counter = counter - 1
    text1.config(text=str(counter))


window = Tk()

text1 = Label(window, text='0', width=10)
button1 = Button(window, text='Counter', width=10)
button1.bind('<Button-1>', increase_value)
button1.bind('<Button-2>', decrease_value)
button1.bind('<Enter>', increase_value)

text1.grid(row=0, column=0)
button1.grid(row=1, column=0)

window.mainloop()

