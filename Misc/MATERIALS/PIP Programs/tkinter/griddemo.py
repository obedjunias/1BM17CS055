from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("400x400")

        self.label = Label(master, text="This is our PACK TRIAL!")
        self.label.grid(row=0,column=0)
        self.label = Label(master, text="This is our first GUI!")
        self.label.grid(row=0,column=1)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1,column=0)

        self.close_button = Button(master, text="Close", command=self.master.destroy)
        self.close_button.grid(row=1,column=1)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
