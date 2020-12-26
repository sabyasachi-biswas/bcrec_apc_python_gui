from tkinter import *
from tkinter import messagebox

def printName1(event):
    messagebox.showinfo("Click","Button1")
    #print("Button 1 was clicked")

def printName2(event):
    print("Button 2 was clicked")

def printName3(event):
    print("Button 3 was clicked")

root = Tk()
root.title("GUI app")
root.geometry("400x400")
#canvas = Canvas(root, width = 450 , height = 500)
#canvas.pack()
# label1 = Label(root, text = "Hello World", fg = "red")
# label1.pack(side = TOP)
topFrame = Frame(root)
topFrame.pack()

# button1 = Button(topFrame, text = "Click", fg = "green", bg = "cyan")
# button1.pack(side = LEFT)
# button2 = Button(topFrame, text = "Click", fg = "red", bg = "cyan")
# button2.pack(side = RIGHT)
# button3 = Button(topFrame, text = "Click", fg = "grey", bg = "cyan")
# button3.pack(side = BOTTOM)


button4 = Button(topFrame, text = "Four", fg = "black", bg = "cyan")
button4.bind("<Button-1>", printName1)
button4.bind("<Button-2>", printName2)
button4.bind("<Button-3>", printName3)

# entry1 = Entry(root)
# entry1.pack()


button4.pack(side = BOTTOM)



label1 = Label(root, text = "Hello World", fg = "red")
label1.pack()

root.mainloop()