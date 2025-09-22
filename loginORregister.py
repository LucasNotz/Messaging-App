from tkinter import *
from tkinter import ttk

class MAlogORreg:
    def __init__(self,root):
        self.root = root
        self.styling()
        self.baseFrame2()
        self.chooseLR()

    def styling(self):
        #colors for ease during mapping
        self.style = ttk.Style()
        self.style.configure("Red.TFrame", background="#ffaaaa")
        self.style.configure("Blue.TFrame", background="#aaaaff")
        self.style.configure("Green.TFrame", background="#fffaaa")
        self.style.configure("White.TFrame", background="ffffff")
        self.style.configure("White.TFrame", background="000000")
        self.style.configure("Big", font=("Comic sans", 12))

    def baseFrame2(self):
        #holds the info for choosing
        self.frameLR = ttk.Frame(self.root, width=400, height=200, style="Red.TFrame")
        self.frameLR.grid_propagate(False)
        self.frameLR.grid(column=0,row=0)

        self.label = ttk.Label(self.frameLR, text="Choose to login or register", font=("Comic sans", 15, "bold")).grid(column=1, row=1,sticky=NSEW, pady=20,padx=20)

    def chooseLR(self):
        #the option
        self.choice = StringVar()
        self.loginOption = ttk.Radiobutton(self.frameLR,text="Login", variable=self.choice, value="l",command=self.chooseButton)
        self.registerOption = ttk.Radiobutton(self.frameLR,text="Register", variable=self.choice, value="r", command=self.chooseButton)
        self.loginOption.grid(column=1,row=2)
        self.registerOption.grid(column=1,row=3)

    def chooseButton(self):
        #verifies the option
        if (self.choice.get() == "l"):
            self.root.quit()
            return "l"

        elif (self.choice.get() == "r"):
            self.root.quit()
            return "r"





    def run(self):
        self.root.mainloop()


