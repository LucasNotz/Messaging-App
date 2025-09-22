from tkinter import *
from tkinter import ttk

class MAregisterGUI:
    #class to be called in main.py
    def __init__(self,root):
        self.root = root
        self.styling()
        self.baseFrame()
        self.registerFrame()
        self.chooseUser()
        self.serverGuiRegister()
        self.clientGuiRegister()
        self.adminGuiRegister()




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
        self.enterPage = ttk.Frame(self.root,padding=(6,6,15,15), width=700,height=300, style="Black.TFrame")
        self.enterPage.grid(column=0,row=0,sticky=(N,W,E,S),pady=5)
        self.enterPage.grid_propagate(False)

        #title for basefame
        self.loginTitle = ttk.Label(self.enterPage, text="Messaging App", font=("Comic sans", 15,"bold")).grid(column=8,row=2,sticky=NSEW,pady=20)

        ###
        ### user login
        ###

    def registerFrame(self):
        #frame on base frame where login things will go
        self.registerFrame = ttk.Frame(self.enterPage, width= 650, height=200,style="Blue.TFrame")
        self.registerFrame.grid_propagate(False)
        self.registerFrame.place(x=20,y=50)

    def chooseUser(self):
        #label for choose user
        self.userType_label = ttk.Label(self.registerFrame, text="Select user type to register", font=("Comic sans", 10, "bold")).grid(column=2,row=4, sticky=NSEW, padx=5,pady=5)

        #radiobutton choose usertype
        self.userType = StringVar()
        self.radioButtonUser = ttk.Frame(self.registerFrame, width=200, height= 300,style="Green.TFrame")
        self.radioButtonUser.grid_propagate(False)
        self.radioButtonUser.grid(column=2,row=6, sticky=NSEW)
        self.chooseUserSH = ttk.Radiobutton(self.radioButtonUser, text="Host", variable=self.userType, value="s", command=self.chooseOption)
        self.chooseUserSC = ttk.Radiobutton(self.radioButtonUser, text="Client", variable=self.userType, value="c", command=self.chooseOption)
        self.chooseUserA = ttk.Radiobutton(self.radioButtonUser, text="Admin", variable=self.userType, value="a", command=self.chooseOption)
        #no () used because it is callable, chooseOption() calls immediately
        self.chooseUserSH.grid(row=0, column=0, sticky="w", pady=2)
        self.chooseUserSC.grid(row=1, column=0, sticky="w", pady=2)
        self.chooseUserA.grid(row=2, column=0, sticky="w", pady=2)

    def buttonCommandPlaceHolder(self):
        print("button pressed3")

    def serverGuiRegister(self):
        #create host login frame
        self.sFrame = ttk.Frame(self.registerFrame, width=300, height= 300,style="Red.TFrame")
        self.sFrame.grid_propagate(False)
        self.sFrame.grid(column=4, row=6,sticky=NSEW)

        #host label
        self.sLabel = ttk.Label(self.sFrame, text="Server", font=("Comic sans", 12, "bold"))
        self.sLabel.grid(column=0,row=0)

        #login info stuff
        self.sUserRegisterLabel = ttk.Label(self.sFrame, text="Register:")
        self.sUserRegisterLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

        self.sUsername = StringVar()
        self.sUserRegisterEntry = ttk.Entry(self.sFrame,width=12,textvariable=self.sUsername)
        self.sUserRegisterEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

        self.sUserPassLabel = ttk.Label(self.sFrame, text="Password:")
        self.sUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

        self.sPass = StringVar()
        self.sUserPassEntry = ttk.Entry(self.sFrame,width=12,textvariable=self.sPass)
        self.sUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

        self.sUserRegisterButton = ttk.Button(self.sFrame,text="Register",command=self.buttonCommandPlaceHolder)
        self.sUserRegisterButton.grid(column=1,row=4)

        #make grid disappear until called uppon
        self.sFrame.grid_forget()

    def clientGuiRegister(self):
        #create host login frame
        self.cFrame = ttk.Frame(self.registerFrame, width=300, height= 300,style="Red.TFrame")
        self.cFrame.grid_propagate(False)
        self.cFrame.grid(column=4, row=6,sticky=NSEW)

        #host label
        self.cLabel = ttk.Label(self.cFrame, text="Client", font=("Comic sans", 12, "bold"))
        self.cLabel.grid(column=0,row=0)

        #login info stuff
        self.cUserRegisterLabel = ttk.Label(self.cFrame, text="Register:")
        self.cUserRegisterLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

        self.cUsername = StringVar()
        self.cUserRegisterEntry = ttk.Entry(self.cFrame,width=12,textvariable=self.cUsername)
        self.cUserRegisterEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

        self.cUserPassLabel = ttk.Label(self.cFrame, text="Password:")
        self.cUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

        self.cPass = StringVar()
        self.cUserPassEntry = ttk.Entry(self.cFrame,width=12,textvariable=self.cPass)
        self.cUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

        self.cUserRegisterButton = ttk.Button(self.cFrame,text="Register",command=self.buttonCommandPlaceHolder)
        self.cUserRegisterButton.grid(column=1,row=4)

        #make grid disappear until called uppon
        self.cFrame.grid_forget()

    def adminGuiRegister(self):
        #create host login frame
        self.aFrame = ttk.Frame(self.registerFrame, width=300, height= 300,style="Red.TFrame")
        self.aFrame.grid_propagate(False)
        self.aFrame.grid(column=4, row=6,sticky=NSEW)

        #host label
        self.aLabel = ttk.Label(self.aFrame, text="Admin", font=("Comic sans", 12, "bold"))
        self.aLabel.grid(column=0,row=0)

        #login info stuff
        self.aUserRegisterLabel = ttk.Label(self.aFrame, text="Register:")
        self.aUserRegisterLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

        self.aUsername = StringVar()
        self.aUserRegisterEntry = ttk.Entry(self.aFrame,width=12,textvariable=self.aUsername)
        self.aUserRegisterEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

        self.aUserPassLabel = ttk.Label(self.aFrame, text="Password:")
        self.aUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

        self.aPass = StringVar()
        self.aUserPassEntry = ttk.Entry(self.aFrame,width=12,textvariable=self.aPass)
        self.aUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

        self.aKey = StringVar()
        self.aKeyEntry = ttk.Entry(self.aFrame, width=6, textvariable=self.aKey)
        self.aKeyEntry.grid(column=0,row=4)

        self.aUserRegisterButton = ttk.Button(self.aFrame,text="Register",command=self.buttonCommandPlaceHolder)
        self.aUserRegisterButton.grid(column=1,row=4)

        #make grid disappear until called uppon
        self.aFrame.grid_forget()

    def chooseOption(self):
        #hides all frames
        self.sFrame.grid_forget()
        self.cFrame.grid_forget()
        self.aFrame.grid_forget()

        #allows to choos between all others
        if (self.userType.get() == "s"):
            self.sFrame.grid(column=4, row=6,sticky=NSEW)
            print("s")
        elif (self.userType.get() == "c"):
            self.cFrame.grid(column=4, row=6,sticky=NSEW)
            print("c")
        elif (self.userType.get() == "a"):
            print("a")
            self.aFrame.grid(column=4, row=6,sticky=NSEW)






    def run(self):
        #runs program
        self.root.mainloop()
