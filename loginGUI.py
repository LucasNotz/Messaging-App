from tkinter import *
from tkinter import ttk
from database import *

class MAloginGUI:
    dbR = MAdatabase()
    #class to be called in main.py
    def __init__(self,root):
        self.root = root
        self.baseFrame()
        self.loginFrame()
        self.chooseUser()
        self.serverGuiLogin()
        self.clientGuiLogin()
        self.adminGuiLogin()
        self.nextPageA()
        self.nextPageC()
        self.nextPageS()





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
        self.enterPage = ttk.Frame(self.root,padding=(6,6,15,15), width=700,height=300)
        self.enterPage.grid(column=0,row=0,sticky=(N,W,E,S),pady=5)
        self.enterPage.grid_propagate(False)

        #title for basefame
        self.loginTitle = ttk.Label(self.enterPage, text="Messaging App", font=("Comic sans", 15,"bold")).grid(column=8,row=2,sticky=NSEW,pady=20)

        ###
        ### user login
        ###

    def loginFrame(self):
        #frame on base frame where login things will go
        self.loginFrame = ttk.Frame(self.enterPage, width= 650, height=200)
        self.loginFrame.grid_propagate(False)
        self.loginFrame.place(x=20,y=50)

    def chooseUser(self):
        #label for choose user
        self.userType_label = ttk.Label(self.loginFrame, text="Select user type to login", font=("Comic sans", 10, "bold")).grid(column=2,row=4, sticky=NSEW, padx=5,pady=5)

        #radiobutton choose usertype
        self.userType = StringVar()
        self.radioButtonUser = ttk.Frame(self.loginFrame, width=200, height= 300)
        self.radioButtonUser.grid_propagate(False)
        self.radioButtonUser.grid(column=2,row=6, sticky=NSEW)
        self.chooseUserSH = ttk.Radiobutton(self.radioButtonUser, text="Server", variable=self.userType, value="s", command=self.chooseOption)
        self.chooseUserSC = ttk.Radiobutton(self.radioButtonUser, text="Client", variable=self.userType, value="c", command=self.chooseOption)
        self.chooseUserA = ttk.Radiobutton(self.radioButtonUser, text="Admin", variable=self.userType, value="a", command=self.chooseOption)
        #no () used because it is callable, chooseOption() calls immediately
        self.chooseUserSH.grid(row=0, column=0, sticky="w", pady=2)
        self.chooseUserSC.grid(row=1, column=0, sticky="w", pady=2)
        self.chooseUserA.grid(row=2, column=0, sticky="w", pady=2)

    def buttonCommandPlaceHolder(self):
        print("button pressed")


    def serverGuiLogin(self):
        #create host login frame
        self.sFrame = ttk.Frame(self.loginFrame, width=300, height= 300)
        self.sFrame.grid_propagate(False)
        self.sFrame.grid(column=4, row=6,sticky=NSEW)

        #host label
        self.sLabel = ttk.Label(self.sFrame, text="Server", font=("Comic sans", 12, "bold"))
        self.sLabel.grid(column=0,row=0)

        #login info stuff
        self.sUserLoginLabel = ttk.Label(self.sFrame, text="Login:")
        self.sUserLoginLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

        self.sUsername = StringVar()
        self.sUserLoginEntry = ttk.Entry(self.sFrame,width=12,textvariable=self.sUsername)
        self.sUserLoginEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

        self.sUserPassLabel = ttk.Label(self.sFrame, text="Password:")
        self.sUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

        self.sPass = StringVar()
        self.sUserPassEntry = ttk.Entry(self.sFrame,width=12,textvariable=self.sPass)
        self.sUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

        self.sUserLoginButton = ttk.Button(self.sFrame,text="Validate",command=lambda:self.dbR.logUserS(self.sUsername,self.sPass))
        self.sUserLoginButton.grid(column=1,row=4)

        #make grid disappear until called uppon
        self.sFrame.grid_forget()

    def clientGuiLogin(self):
        #create host login frame
        self.cFrame = ttk.Frame(self.loginFrame, width=300, height= 300)
        self.cFrame.grid_propagate(False)
        self.cFrame.grid(column=4, row=6,sticky=NSEW)

        #host label
        self.cLabel = ttk.Label(self.cFrame, text="Client", font=("Comic sans", 12, "bold"))
        self.cLabel.grid(column=0,row=0)

        #login info stuff
        self.cUserLoginLabel = ttk.Label(self.cFrame, text="Login:")
        self.cUserLoginLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

        self.cUsername = StringVar()
        self.cUserLoginEntry = ttk.Entry(self.cFrame,width=12,textvariable=self.cUsername)
        self.cUserLoginEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

        self.cUserPassLabel = ttk.Label(self.cFrame, text="Password:")
        self.cUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

        self.cPass = StringVar()
        self.cUserPassEntry = ttk.Entry(self.cFrame,width=12,textvariable=self.cPass)
        self.cUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

        self.cUserLoginButton = ttk.Button(self.cFrame,text="Validate",command=lambda:self.dbR.logUserC(self.cUsername,self.cPass))
        self.cUserLoginButton.grid(column=1,row=4)

        #make grid disappear until called uppon
        self.cFrame.grid_forget()

    def adminGuiLogin(self):
        #create host login frame
        self.aFrame = ttk.Frame(self.loginFrame, width=300, height= 300)
        self.aFrame.grid_propagate(False)
        self.aFrame.grid(column=4, row=6,sticky=NSEW)

        #host label
        self.aLabel = ttk.Label(self.aFrame, text="Admin", font=("Comic sans", 12, "bold"))
        self.aLabel.grid(column=0,row=0)

        #login info stuff
        self.aUserLoginLabel = ttk.Label(self.aFrame, text="Login:")
        self.aUserLoginLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

        self.aUsername = StringVar()
        self.aUserLoginEntry = ttk.Entry(self.aFrame,width=12,textvariable=self.aUsername)
        self.aUserLoginEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

        self.aUserPassLabel = ttk.Label(self.aFrame, text="Password:")
        self.aUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

        self.aPass = StringVar()
        self.aUserPassEntry = ttk.Entry(self.aFrame,width=12,textvariable=self.aPass)
        self.aUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

        self.aUserLoginButton = ttk.Button(self.aFrame,text="Validate",command=lambda:self.dbR.logUserA(self.aUsername,self.aPass))
        self.aUserLoginButton.grid(column=1,row=4)

        #make grid disappear until called uppon
        self.aFrame.grid_forget()


    def nextPageS(self):
        self.btn = ttk.Button(self.sFrame,text="Chat",command=lambda:self.close()).grid(column=3,row=3,sticky=NSEW)

    def nextPageC(self):
        self.btn = ttk.Button(self.cFrame,text="Chat",command=lambda:self.close()).grid(column=3,row=3,sticky=NSEW)

    def nextPageA(self):
        self.btn = ttk.Button(self.aFrame,text="Chat",command=lambda:self.close()).grid(column=3,row=3,sticky=NSEW)

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


    def close(self):
        self.enterPage.quit()


    def run(self):
        #runs program
        self.root.mainloop()
