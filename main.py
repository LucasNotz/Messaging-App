from tkinter import *
from tkinter import ttk

from loginGUI import *
from loginORregister import *
from registerGUI import *
from database import *

from adminGUI import *
from serverGUI import *
from clientGUI import *

#creates tables if none exist
db = MAdatabase()
MAdatabase.closeUserSession()
#garantees thats active user can be established

#create frame prime (autobots, assemble)

root = Tk()
root.title("MessagingApp")





#runs "login or register" gui
firstPage = MAlogORreg(root)
firstPage.run()

#it quits itself when choice is made
var1 = False

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
    var1 = True


currentUser = MAdatabase.retriveActiveUser()
user = currentUser[0][0]
tipo = currentUser[0][1]
if ((user and tipo) and var1):
    loginPage2.close()
else:
    loginPage.close()


if (tipo == "s"):
    serverPage = MAserverGUI(root)
    serverPage.run()
elif (tipo == "c"):
    clientPage = MAclientGUI(root)
    clientPage.run()
elif (tipo == "a"):
    adminPage = MAadminGUI(root)
    adminPage.run()









