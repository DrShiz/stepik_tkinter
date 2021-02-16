from tkinter import *

window = Tk()
window.geometry('400x500')


def brush(event):
    cnv.create_oval(event.x - 5,
                    event.y - 5,
                    event.x + 5,
                    event.y + 5,
                    fill='red',
                    outline='red')


cnv = Canvas(window)
cnv.bind('<B1-Motion>', brush)
# cnv.create_oval(50, 50, 300, 300, fill='blue', width=10, outline='grey')
# cnv.create_line(100, 130, 250, 300, width=20)
# cnv.create_arc(10, 50, 300, 300, width=10)
# cnv.create_text(150, 400, text='Hello World\nHi, there', justify=CENTER, font=('Times', '40', 'italic'))
cnv.pack(fill=BOTH, expand=1)

window.mainloop()
