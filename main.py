from tkinter import *
from tkinter import ttk

from loginGUI import *
from loginORregister import *
from registerGUI import *
from database import *

#creates tables if none exist
MAdatabase.createTables()
#create frame prime (autobots, assemble)

root = Tk()

## test


currentPage= ""

#runs "login or register" gui
firstPage = MAlogORreg(root)
firstPage.run()
#it quits itself when choice is made

#decides to go to register or login
if (firstPage.choice.get() == "l"):
    loginPage = MAloginGUI(root)
    loginPage.run()
elif (firstPage.choice.get() == "r"):
    registerPage = MAregisterGUI(root)
    registerPage.run()
    loginPage2 = MAloginGUI(root)
    loginPage2.run()












