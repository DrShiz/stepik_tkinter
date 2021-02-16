from tkinter import *


def clicked():
    text = entry_text.get()
    text1.config(text=f'Hello, {text}! How r u?')
    button1.config(text='Clicked!', bg='red', fg='green')


window = Tk()
window.title("Clicking application")
window.geometry("300x350")

text1 = Label(window, text='Enter ur name')
entry_text = Entry(window)
text1.pack()
entry_text.pack()
button1 = Button(window, text="Click me!", command=clicked)
button1.pack()

window.mainloop()


