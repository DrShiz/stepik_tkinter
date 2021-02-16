from tkinter import *

window = Tk()
top_frame = Frame(window)
bottom_frame = Frame(window)
text1 = Label(top_frame, text='text1')
button1 = Button(bottom_frame, text='Button1')
button2 = Button(bottom_frame, text='Button2')
button3 = Button(bottom_frame, text='Button3')
button4 = Button(bottom_frame, text='Button4')
text2 = Label(bottom_frame, text='text2')

top_frame.pack()
bottom_frame.pack()
text1.pack()
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)
text2.grid(row=0, column=2, rowspan=2)

window.mainloop()
