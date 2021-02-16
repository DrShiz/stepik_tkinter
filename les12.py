from tkinter import *
from tkinter import messagebox


def confirm():
    print(clr.get())
    if yes_no.get() == 1:
        messagebox.showinfo('Hello', 'You have chosen '+clr.get())
    else:
        messagebox.showwarning('No no', 'Please put a tick')


window = Tk()
values = ['Red', 'Green', 'Yellow', 'Blue', 'Black']
yes_no = IntVar()
clr = StringVar()
clr.set('Red')

for i in range(5):
    lbl = Label(window, text=values[i])
    c = Radiobutton(variable=clr, value=values[i])
    lbl.grid(row=i+1, column=0)
    c.grid(row=i+1, column=1)

yes_no_lbl = Label(window, text='Yes/No')
yes_no_cbut = Checkbutton(variable=yes_no, onvalue=1)
yes_no_lbl.grid(row=6, column=0)
yes_no_cbut.grid(row=6, column=0)

button = Button(window, text='Confirm', command=confirm)
button.grid(row=7, column=0, columnspan=2)

window.mainloop()
