import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect("MessageApp.db")
cursor = conn.cursor()

cursor.execute("""
    create table if not exists
"""")
