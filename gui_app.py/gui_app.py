from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class NewClass:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        printButton = Button(frame, text = "Print Message", command = self.printMessage)
        printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack()

    def printMessage(self):
            print("Message worked")


def printName1():
    messagebox.showinfo("Click","Button1")
    
    #print("Button 1 was clicked")

def printName2(event):
    #print("Button 2 was clicked")
    root.filename = filedialog.askopenfilename(initialdir = "/Images", title = "Select a File")

def printName3(event):
    print("Button 3 was clicked")

root = Tk()
root.title("GUI app")
root.geometry("400x400")

object1 = NewClass(root)
object1.quitButton.bind("<Button-2>", printName3)

#root.filename = filedialog.askopenfilename(initialdir = "/Images", title = "Select a File")
#canvas = Canvas(root, width = 450 , height = 500)
#canvas.pack()
# label1 = Label(root, text = "Hello World", fg = "red")
# label1.pack(side = TOP)
# topFrame = Frame(root)
# topFrame.pack()

# button1 = Button(root, text = "Click", fg = "green", bg = "cyan", command = printName1)
# button1.bind("<Button-2>", printName2)
# button1.bind("<Button-3>", printName3)
# button1.pack(anchor = CENTER)


# button2 = Button(topFrame, text = "Click", fg = "red", bg = "cyan")
# button2.pack(side = RIGHT)
# button3 = Button(topFrame, text = "Click", fg = "grey", bg = "cyan")
# button3.pack(side = BOTTOM)


# button4 = Button(topFrame, text = "Four", fg = "black", bg = "cyan")
# button4.bind("<Button-1>", printName1)
# button4.bind("<Button-2>", printName2)
# button4.bind("<Button-3>", printName3)

# entry1 = Entry(root)
# entry1.pack()


#button4.pack(side = BOTTOM)



# label1 = Label(root, text = "Hello World", fg = "red")
# label1.pack()

root.mainloop()