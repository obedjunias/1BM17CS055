from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("700x700")

        self.label = Label(master, text="This is our PACK TRIAL!")
        self.label.place(x=100,y=100)
        self.label = Label(master, text="This is our first GUI!")
        self.label.place(x=200,y=200)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.place(x=300,y=300,width=200,height=200)

        self.close_button = Button(master, text="Close", command=self.master.destroy)
        self.close_button.place(relx=0.5,rely=0.5, in_=self.greet_button)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
