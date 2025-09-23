from tkinter import *
from tkinter import ttk

from loginGUI import *
from loginORregister import *
from registerGUI import *
from database import *

#creates tables if none exist
db = MAdatabase()

#create frame prime (autobots, assemble)

root = Tk()

## test






#runs "login or register" gui
firstPage = MAlogORreg(root)
firstPage.run()

#it quits itself when choice is made


#decides to go to register or login
if (firstPage.choice.get() == "l"):
    loginPage = MAloginGUI(root)
    loginPage.run()

elif (firstPage.choice.get() == "r"):
    #allows for register then login
    registerPage = MAregisterGUI(root)
    registerPage.run()
    loginPage2 = MAloginGUI(root)
    loginPage2.run()

print(MAdatabase.retriveActiveUser())










