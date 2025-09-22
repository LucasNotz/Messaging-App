from tkinter import *
from tkinter import ttk

from loginGUI import MAloginGUI
from loginORregister import MAlogORreg
from registerGUI import MAregisterGUI

#main window where class instances will appear
adminKey="12345"

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














