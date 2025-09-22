from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Messaging App")

#for development
style = ttk.Style()
style.configure("Red.TFrame", background="#ffaaaa")
style.configure("Blue.TFrame", background="#aaaaff")
style.configure("Green.TFrame", background="#fffaaa")

#setting opening page frame
enterPage = ttk.Frame(root,padding=(6,6,15,15), width=700,height=500, style="Red.TFrame")
enterPage.grid(column=0,row=0,sticky=(N,W,E,S),pady=5)
enterPage.grid_propagate(False)

#title
loginTitle = ttk.Label(enterPage, text="Messaging App", font=("Comic sans", 15,"bold")).grid(column=8,row=2,sticky=NSEW,pady=20)

##############################3
#register or login

#login frame
loginFrame = ttk.Frame(enterPage, width= 650, height=400,style="Blue.TFrame")
loginFrame.grid_propagate(False)
loginFrame.place(x=20,y=50)
#usertype label
userType_label = ttk.Label(loginFrame, text="Select user type", font=("Comic sans", 10, "bold")).grid(column=2,row=4, sticky=NSEW, padx=5,pady=5)

#radiobutton choose usertype
userType = StringVar()
radioButtonUser = ttk.Frame(loginFrame, width=200, height= 300,style="Green.TFrame")
radioButtonUser.grid_propagate(False)
radioButtonUser.grid(column=2,row=6, sticky=NSEW)
chooseUserSH = ttk.Radiobutton(radioButtonUser, text="Host", variable=userType, value="h")
chooseUserSC = ttk.Radiobutton(radioButtonUser, text="Client", variable=userType, value="c")
chooseUserA = ttk.Radiobutton(radioButtonUser, text="Admin", variable=userType, value="a")
chooseUserSH.grid(row=0, column=0, sticky="w", pady=2)
chooseUserSC.grid(row=1, column=0, sticky="w", pady=2)
chooseUserA.grid(row=2, column=0, sticky="w", pady=2)

#server host frame login and hide
sFrame = ttk.Frame(loginFrame, width=300, height= 300,style="Red.TFrame")
sFrame.grid_propagate(False)
sFrame.grid(column=4, row=6,sticky=NSEW)

sLabel = ttk.Label(sFrame, text="Host", font=("Comic sans", 12, "bold"))
sLabel.grid(column=0,row=0)

sUserLoginLabel = ttk.Label(sFrame, text="Login:")
sUserLoginLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

sUsername = StringVar()
sUserLoginEntry = ttk.Entry(sFrame,width=12,textvariable=sUsername)
sUserLoginEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

sUserPassLabel = ttk.Label(sFrame, text="Password:")
sUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

sPass = StringVar()
sUserPassEntry = ttk.Entry(sFrame,width=12,textvariable=sPass)
sUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

sUserLoginButton = ttk.Button(sFrame,text="Validate")
sUserLoginButton.grid(column=1,row=4)

sFrame.grid_forget()

#server client frame login and hide
cFrame = ttk.Frame(loginFrame, width=300, height= 300,style="Red.TFrame")
cFrame.grid_propagate(False)
cFrame.grid(column=4, row=6,sticky=NSEW)

cLabel = ttk.Label(cFrame, text="Client", font=("Comic sans", 12, "bold"))
cLabel.grid(column=0,row=0)

cUserLoginLabel = ttk.Label(cFrame, text="Login:")
cUserLoginLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

cUsername = StringVar()
cUserLoginEntry = ttk.Entry(cFrame,width=12,textvariable=cUsername)
cUserLoginEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

cUserPassLabel = ttk.Label(cFrame, text="Password:")
cUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

cPass = StringVar()
cUserPassEntry = ttk.Entry(cFrame,width=12,textvariable=cPass)
cUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

cUserLoginButton = ttk.Button(cFrame,text="Validate")
cUserLoginButton.grid(column=1,row=4)

cFrame.grid_forget()

#server admin frame login and hide
aFrame = ttk.Frame(loginFrame, width=300, height= 300,style="Red.TFrame")
aFrame.grid_propagate(False)
aFrame.grid(column=4, row=6,sticky=NSEW)

aLabel = ttk.Label(aFrame, text="Admin", font=("Comic sans", 12, "bold"))
aLabel.grid(column=0,row=0)

aUserLoginLabel = ttk.Label(aFrame, text="Login:")
aUserLoginLabel.grid(column=0,row=2,sticky=NSEW,pady=10,padx=10)

aUsername = StringVar()
aUserLoginEntry = ttk.Entry(aFrame,width=12,textvariable=aUsername)
aUserLoginEntry.grid(column=1, row=2,sticky=NSEW,pady=10,padx=10)

aUserPassLabel = ttk.Label(aFrame, text="Password:")
aUserPassLabel.grid(column=0,row=3,sticky=NSEW,pady=10,padx=10)

aPass = StringVar()
aUserPassEntry = ttk.Entry(aFrame,width=12,textvariable=aPass)
aUserPassEntry.grid(column=1, row=3,sticky=NSEW,pady=10,padx=10)

aUserLoginButton = ttk.Button(aFrame,text="Validate")
aUserLoginButton.grid(column=1,row=4)

aFrame.grid_forget()


#runs program
root.mainloop()


