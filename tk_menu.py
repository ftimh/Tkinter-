from Tkinter import *

# doesn't work on Mac

def doNothing():
	print("Nothing....")


root = Tk()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "New project", command = doNothing)
subMenu.add_command(label = "Save", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command = doNothing)

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Create", command = doNothing)

root.mainloop()