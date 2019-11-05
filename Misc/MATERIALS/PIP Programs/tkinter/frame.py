from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.grid()
        self.label = Label(master, text="This is our first GUI!")
        self.label.grid()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid()
        self.count=0
        self.close_button = Button(master, text="Close", command=self.master.destroy)
        self.close_button.grid()

    def greet(self):
        #print("Greetings!")
        self.count+=1
        self.greet_button["text"]="Clicked:",self.count," times"

root = Tk()
fra1=Frame(root)
root.title("A simple GUI")
root.geometry("400x400")
my_gui = MyFirstGUI(fra1)
root.mainloop()
