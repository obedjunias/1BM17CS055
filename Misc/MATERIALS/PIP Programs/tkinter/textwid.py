from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("400x400")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.deltext)#command=self.master.destroy)
        self.close_button.pack()

        self.te=Entry(master,width="20")
        self.te.pack()

        self.te1=Text(master,width=20,height="10")
        self.te1.pack()

        

    def greet(self):
        self.te1.insert(1.1,"Hello")

    def deltext(self):
        self.te1.delete(1.1,END)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
