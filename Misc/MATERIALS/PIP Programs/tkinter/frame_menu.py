from tkinter import *
from tkinter import messagebox

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        # Creating Menubar 
        menubar = Menu(master) 
        self.master.config(menu=menubar)
        # Adding File Menu and commands 
        file = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='File', menu = file) 
        file.add_command(label ='New File', command =self.nfil ) 
        file.add_command(label ='Open...', command = self.ope) 
        file.add_command(label ='Save', command = self.sav) 
        file.add_separator() 
        file.add_command(label ='Exit', command = root.destroy) 
  
        # Adding Edit Menu and commands 
        edit = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Edit', menu = edit) 
        edit.add_command(label ='Cut', command = None) 
        edit.add_command(label ='Copy', command = None) 
        edit.add_command(label ='Paste', command = None) 
        edit.add_command(label ='Select All', command = None) 
        edit.add_separator() 
        edit.add_command(label ='Find...', command = None) 
        edit.add_command(label ='Find again', command = None) 
  
        # Adding Help Menu 
        help_ = Menu(menubar, tearoff = 1) 
        menubar.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='Tk Help', command = None) 
        help_.add_command(label ='Demo', command = None) 
        help_.add_separator() 
        help_.add_command(label ='About Tk', command = None) 
    
    def nfil(self):
        messagebox.showinfo("Menu info","New option pressed")
    def ope(self):
        messagebox.showinfo("Menu info","Open option pressed")
    def sav(self):
        messagebox.showinfo("Menu info","Save option pressed")

root = Tk()
fra1=Frame(root)
root.title("A simple GUI")
root.geometry("600x600")
my_gui = MyFirstGUI(root)
root.mainloop()
