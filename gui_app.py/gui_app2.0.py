from tkinter import *

app = Tk()
app.title("New Gui App")
app.geometry("400x400")

class gui_app:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()

        self.entry1 = Entry(master)
        self.entry1.pack()

        self.button1 = Button(app, text = "New window", command = self.button_click)
        self.button1.pack()

        button4 = Button(app, text = "Print" , command = self.button_print)
        button4.pack()

    def button_print(self):
        text = self.entry1.get()
        self.printfun(text)

    def button_click(self):
        text = self.entry1.get()
        self.new_window(text)

    def new_window(self, string):
        new_window = Tk()
        new_window.title("New Window")
        new_window.geometry("200x200")

        button2 = Button(new_window, text = "Quit" , command = new_window.destroy)
        button2.pack()
        button3 = Button(new_window, text = "Print" , command = self.printfun(string))
        # button3.bind("<Button-1>,",self.printfun(string))
        button3.pack()

    def printfun(self,text):
        print(text)



obj1 = gui_app(app)

app.mainloop()