from tkinter import *

window = Tk()
window.title('Menu Bar App')
window.geometry('400x300')


def print_hello():
    print("Hello World")


menu_bar = Menu(window)
file_menu = Menu(menu_bar)
save_menu = Menu(file_menu)

menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = print_hello)
file_menu.add_command(label = "Open", command = print_hello)

file_menu.add_separator()
file_menu.add_cascade(label = "Save", menu = save_menu)
save_menu.add_command(label = "Save...")
save_menu.add_command(label = "Save as...")

window.mainloop()
