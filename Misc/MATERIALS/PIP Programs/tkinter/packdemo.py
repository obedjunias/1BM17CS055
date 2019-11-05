from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("400x400")

        self.label = Label(master, text="This is our PACK TRIAL!")
        self.label.pack(side=TOP)
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack(side=RIGHT)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="Close", command=self.master.destroy)
        self.close_button.pack(side=BOTTOM)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
