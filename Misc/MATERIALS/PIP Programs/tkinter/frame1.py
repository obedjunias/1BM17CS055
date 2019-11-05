from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
       
        self.c1=True
        self.c2=False
        self.cb1 = Checkbutton(master, text="COA", variable=self.c1,command=self.che)
        self.cb1.grid(row=0,column=0)

        self.cb2 = Checkbutton(master, text="DS", variable=self.c2,command=self.che)
        self.cb2.grid(row=0,column=1)
        
        self.rad1 = Radiobutton(master, text="COA", variable=self.c1,command=self.rad)
        self.rad1.grid(row=1,column=0)

        self.rad1 = Radiobutton(master, text="DS", variable=self.c2,command=self.rad)
        self.rad1.grid(row=1,column=1)

        self.t1=Text(master,width=50, height=5,wrap=WORD)
        self.t1.grid(row=2,column=0)
                     
    def rad(self):
        print("Radiobutton selected")
    def che(self):
        print("Checkbutton selected")


    

root = Tk()

root.title("A simple GUI")
root.geometry("700x700")
my_gui = MyFirstGUI(root)
root.mainloop()
