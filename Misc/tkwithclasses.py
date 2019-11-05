from tkinter import *

class MyClass:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print",command=self.PrintButton)
        self.quitButton = Button(frame,text="Quit",command=frame.quit)
        self.printButton.pack(side=LEFT)
        self.quitButton.pack(side=RIGHT)

    def PrintButton(self):
        print("Printing.....")        



root = Tk()
ob1 = MyClass(root)
root.mainloop()