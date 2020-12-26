from tkinter import *

def printName(event):
    print("Sabyasachi Biswas")

root = Tk()
root.title("GUI app")
canvas = Canvas(root, width = 450 , height = 500)
canvas.pack()
label1 = Label(root, text = "Hello World", fg = "red")
label1.pack(side = TOP)
topFrame = Frame(root)
topFrame.pack()

button1 = Button(canvas, text = "Click", fg = "green", bg = "cyan")
button1.pack(side = LEFT)
button2 = Button(topFrame, text = "Click", fg = "red", bg = "cyan")
button2.pack(side = RIGHT)
button3 = Button(topFrame, text = "Click", fg = "grey", bg = "cyan")
button3.pack(side = BOTTOM)


button4 = Button(topFrame, text = "Four", fg = "black", bg = "cyan")
button4.bind("<Button-1>", printName)
button4.pack(side = BOTTOM)



label1 = Label(root, text = "Hello World", fg = "red")
label1.pack()

root.mainloop()