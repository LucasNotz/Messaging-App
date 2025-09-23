from tkinter import *
from tkinter import ttk

class MAserverGUI:

    def __init__(self):
        self.root = root
        self.styling()
        self.baseFrame()


    def styling(self):
        #colors for ease during mapping
        self.style = ttk.Style()
        self.style.configure("Red.TFrame", background="#ffaaaa")
        self.style.configure("Blue.TFrame", background="#aaaaff")
        self.style.configure("Green.TFrame", background="#fffaaa")
        self.style.configure("White.TFrame", background="ffffff")
        self.style.configure("White.TFrame", background="000000")

    def baseFrame(self):
        #frame where all widgets will go
        self.enterPage = ttk.Frame(self.root,padding=(6,6,15,15), width=700,height=350, style="Black.TFrame")
        self.enterPage.grid(column=0,row=0,sticky=(N,W,E,S),pady=5)
        self.enterPage.grid_propagate(False)


    def close(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()
