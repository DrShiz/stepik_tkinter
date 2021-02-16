from tkinter import *


def submit():
    text.config(text='Logged in')


def clear():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


def close():
    window.destroy()


window = Tk()
window.title('Learning GRID')

username_label = Label(window, text='Username:')
password_label = Label(window, text='Password:')
username_entry = Entry(window)
password_entry = Entry(window)
submit_button = Button(window, text='Submit', command=submit)
clear_button = Button(window, text='Clear', command=clear)
close_button = Button(window, text='Close', command=close)
text = Label(window, text='')

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1, columnspan=2)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1, columnspan=2)
submit_button.grid(row=2, column=0, ipadx=20)
clear_button.grid(row=2, column=1, ipadx=20)
close_button.grid(row=2, column=2, ipadx=20)
text.grid(row=3, column=0, columnspan=3)

window.mainloop()
