import tkinter as tk


def but_click(number):
    e.insert(END, number)


window = tk.Tk()

e = tk.Entry(window)
e.pack()

b1 = tk.Button(window, text='1', command=lambda: but_click(1))
b2 = tk.Button(window, text='2', command=lambda: but_click(2))

b1.pack()
b2.pack()

window.mainloop()
