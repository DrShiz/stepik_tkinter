from tkinter import *


def hello(event):
    text1.config(bg='green')


def bye(event):
    text1.config(bg='red')


window = Tk()

text1 = Label(window, width=30, height=30, text='', bg='red')
text1.pack()
text1.bind('<Right>', hello)
text1.bind('<Left>', bye)

window.mainloop()
