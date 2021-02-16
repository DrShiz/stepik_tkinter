from tkinter import *


def clicked():
    name = name_entry.get()
    surname = surname_entry.get()
    message_label.config(text=f'Welcome, {name} {surname}! You have registered')


window = Tk()
window.title("Clicking application")
top_frame = Frame(window)
labels_frame = Frame(top_frame)
enries_frame = Frame(top_frame)
bottom_frame = Frame(window)
window.geometry("300x350")
name_label = Label(labels_frame, text='Name')
surname_label = Label(labels_frame, text='Surname')
name_entry = Entry(enries_frame)
surname_entry = Entry(enries_frame)
reg_button = Button(bottom_frame, text='Register', command=clicked)
message_label = Label(bottom_frame, text='')

name_label.pack()
surname_label.pack()
name_entry.pack()
surname_entry.pack()
reg_button.pack()
message_label.pack()
top_frame.pack()
labels_frame.pack(side=LEFT)
enries_frame.pack()
bottom_frame.pack()

window.mainloop()
