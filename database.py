import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import hashlib


class MAdatabase:
    adminKey="12345"


    def hash_password(password):
        password_bytes = password.encode("utf-8")
        hashed = hashlib.sha256(password_bytes).hexdigest()
        return hashed


    def createTables():
        #connects to db
        conn = sqlite3.connect("MessagingApp.db")
        #db manipulator opens
        cursor = conn.cursor()

        #creating tables for info
        cursor.execute("""
            create table if not exists user_server (
                id integer primary key autoincrement,
                username text unique not null,
                password_hash text not null
        )
        """)

        cursor.execute("""
            create table if not exists user_client (
                id integer primary key autoincrement,
                username text unique not null,
                password_hash text not null
        )
        """)

        cursor.execute("""
            create table if not exists user_admin (
                id integer primary key autoincrement,
                username text unique not null,
                password_hash text not null
        )
        """)

        #db manipulator efetiva
        conn.commit()
        #db man closes
        conn.close()

    def createUserS(self,sUsername,sPass):
        username = sUsername.get()
        password = sPass.get()

        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()

        if not username or not password:
            messagebox.showwarning("input error", "enter both username and password")
            return

        password_hashed = hash_password(password)

        try:
            #parameterized query = safer
            cursor.execute(
                "insert into user_server (username, password_hash) values (?, ?)", (username, password_hashed)
                )
            conn.commit()
            messagebox.showinfo("Great Success", f"Server user {username} created")
            sUsername.set("")
            sPass.set("")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Server user already exists")

        conn.close()

    def createUserC(self,cUsername,cPass):
        username = cUsername.get()
        password = cPass.get()

        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()

        if not username or not password:
            messagebox.showwarning("input error", "enter both username and password")
            return

        password_hashed = hash_password(password)

        try:
            #parameterized query = safer
            cursor.execute(
                "insert into user_client (username, password_hash) values (?, ?)", (username, password_hashed)
                )
            conn.commit()
            messagebox.showinfo("Great Success", f"Client user {username} created")
            cUsername.set("")
            cPass.set("")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Client user already exists")

        conn.close()

    def createUserA(self,aUsername, aPass, aKey):
        username = aUsername.get()
        password = aPass.get()
        key = aKey.get()

        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()

        if not username or not password or not (key == self.adminKey):
            messagebox.showwarning("input error", "enter username, password and key")
            return

        password_hashed = hash_password(password)

        try:
            #parameterized query = safer
            cursor.execute(
                "insert into user_admin (username, password_hash) values (?, ?)", (username, password_hashed)
                )
            conn.commit()
            messagebox.showinfo("Great Success", f"Admin user {username} created")
            aUsername.set("")
            aPass.set("")
            aKey.set("")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Admin user already exists")

        conn.close()











