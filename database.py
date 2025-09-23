import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import hashlib


class MAdatabase:
    adminKey="12345"
    def hash_password(self, password):
        password_bytes = password.encode("utf-8")
        hashed = hashlib.sha256(password_bytes).hexdigest()
        return hashed




    def userSession():
        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()
        cursor.execute("""
            create table if not exists active (
                num int primary key not null,
                username text unique not null,
                user_type text not null
        )
        """)
        conn.commit()
        conn.close()

    def openUserSession(self,username, usertype):
        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()
        num = 1
        cursor.execute(
            "insert into active (num ,username, user_type) values (?,?, ?)", (num, username, usertype)
            )
        conn.commit()
        conn.close()

    def closeUserSession():
        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()
        cursor.execute(
            "delete from active"
            )
        conn.commit()
        conn.close()


    def retriveActiveUser():
        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()
        cursor.execute(
            "select username, user_type from active where num =1"
            )
        user = cursor.fetchall()

        conn.commit()
        conn.close()

        return user

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

        password_hashed = self.hash_password(password)

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

        password_hashed = self.hash_password(password)

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

        password_hashed = self.hash_password(password)

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

    def logUserS(self, sUsername, sPass):
        username = sUsername.get()
        password = sPass.get()

        userLoggedType = StringVar()
        userLoggedUser = StringVar()

        password_hashed = self.hash_password(password)

        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()

        cursor.execute(
            "select * from user_server where username = ? and password_hash = ?", (username,password_hashed)
            )
        result = cursor.fetchone()

        conn.close()

        if result:
            userLoggedType.set("s")
            userLoggedUser.set(f"{username}")
            self.openUserSession(userLoggedUser.get(),userLoggedType.get())
            messagebox.showinfo("Success", f"Welcome {username}")


        else:
            messagebox.showerror("Login failed", ("Try again"))


    def logUserC(self, cUsername, cPass):
        username = cUsername.get()
        password = cPass.get()

        userLoggedType = StringVar()
        userLoggedUser = StringVar()

        password_hashed = self.hash_password(password)

        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()

        cursor.execute(
            "select * from user_client where username = ? and password_hash = ?", (username,password_hashed)
            )
        result = cursor.fetchone()

        conn.close()

        if result:
            messagebox.showinfo("Success", f"Welcome {username}")
            userLoggedType.set("c")
            userLoggedUser.set(f"{username}")
            self.openUserSession(userLoggedUser.get(),userLoggedType.get())

        else:
            messagebox.showerror("Login failed", ("Try again"))


    def logUserA(self, aUsername, aPass):
        username = aUsername.get()
        password = aPass.get()

        userLoggedType = StringVar()
        userLoggedUser = StringVar()

        password_hashed = self.hash_password(password)

        conn = sqlite3.connect("MessagingApp.db")
        cursor = conn.cursor()

        cursor.execute(
            "select * from user_admin where username = ? and password_hash = ?", (username,password_hashed)
            )
        result = cursor.fetchone()

        conn.close()

        if result:
            messagebox.showinfo("Success", f"Welcome {username}")
            userLoggedType.set("a")
            userLoggedUser.set(f"{username}")
            self.openUserSession(userLoggedUser.get(),userLoggedType.get())


        else:
            messagebox.showerror("Login failed", ("Try again"))
























