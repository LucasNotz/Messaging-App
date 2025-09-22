from tkinter import *
from tkinter import ttk

from loginGUI import *
from loginORregister import *
from registerGUI import *
from database import *

#creates tables if none exist
MAdatabase.createTables()

root = Tk()

#runs "login or register" gui
firstPage = MAlogORreg(root)
firstPage.run()
if (firstPage.choice.get() == "l"):
    loginPage = MAloginGUI(root)
    loginPage.run()
elif (firstPage.choice.get() == "r"):
    registerPage = MAregisterGUI(root)
    registerPage.run()














