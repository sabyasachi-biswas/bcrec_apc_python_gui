from tkinter import *

root = Tk()
label1 = Label(root, text = "Hello World", fg = "red")
label1.pack(side = TOP)
topFrame = Frame(root)
topFrame.pack()

button1 = Button(topFrame, text = "Click", fg = "green", bg = "cyan")
button1.pack(side = LEFT)
button2 = Button(topFrame, text = "Click", fg = "red", bg = "cyan")
button2.pack(side = RIGHT)
button3 = Button(topFrame, text = "Click", fg = "grey", bg = "cyan")
button3.pack(side = BOTTOM)

label1 = Label(root, text = "Hello World", fg = "red")
label1.pack()

root.mainloop()