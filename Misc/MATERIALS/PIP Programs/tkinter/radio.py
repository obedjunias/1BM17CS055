import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

v = tk.IntVar()
v1=tk.IntVar()
v2=tk.IntVar()
v3=tk.IntVar()

'''

v = tk.BooleanVar()
v1=tk.BooleanVar()
v2=tk.BooleanVar(value=True)
v3=tk.BooleanVar()
v3.set(True)
'''

tk.Label(root, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
r1=tk.Radiobutton(root, 
              text="Python",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
r2=tk.Radiobutton(root, 
              text="Perl",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)

r3=tk.Radiobutton(root, 
              text="P1",
              padx = 20, 
              variable=v3, 
              value=1).pack(anchor=tk.W)
r4=tk.Radiobutton(root, 
              text="P2",
              padx = 20, 
              variable=v3, 
              value=2).pack(anchor=tk.W)

c1=tk.Checkbutton(root, 
              text="PHP",
              padx = 20, 
              variable=v1, 
              onvalue=3, offvalue=4).pack(anchor=tk.W)
c2=tk.Checkbutton(root, 
              text="Javascript",
              padx = 20, 
              variable=v2, 
              onvalue=3, offvalue=4).pack(anchor=tk.W)

root.mainloop()
