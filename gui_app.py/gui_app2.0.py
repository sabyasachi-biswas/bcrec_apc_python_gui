from tkinter import *

app = Tk()
app.title("New Gui App")
app.geometry("400x400")

class gui_app:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()

        button1 = Button(app, text = "New window", command = self.new_window)
        button1.pack()

    def new_window(self):
        new_window = Tk()
        new_window.title("New Window")
        new_window.geometry("200x200")
        button2 = Button(new_window, text = "Quit" , command = new_window.quit)
        button2.pack()



obj1 = gui_app(app)

app.mainloop()