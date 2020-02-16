import os
# import modules
import sys
from tkinter import *
from tkinter import ttk
import pymysql
import time
import sqlite3
import random
import datetime
import tempfile
import tkinter.messagebox
from tkinter import messagebox
import database
from subprocess import call
import tkinter_nav as tknav
import tkinter as tk


class App(tknav.Wrapper):

    def __init__(self, ):
        tknav.Wrapper.__init__(
            self,
            pages=[LoginPage, HomePage, RegisterPage],
            start_state={'previous_page': None}
        )
        width = 1350
        height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.resizable(0, 0)
        self.config(bg="#6666ff")
        self.title("Hospital Management System")
        self.show_page('login_page')


# ==========================================Login Page=================================
class LoginPage(tknav.Page):

    def __init__(self, parent):
        tknav.Page.__init__(self, parent, 'login_page')

        tk.Label(self, text='Page One').pack()
        tk.Button(self, text='Navigate to Page Two', command=lambda: self.__navigate()).pack()
        self.LabelTile = Label(self, text='Login', font=('arial', 50, 'bold'), bd=20).pack()

        manage_frame = Frame(self, bd=4, relief=RIDGE, bg="crimson")
        manage_frame.place(x=20, y=150, width=1010, height=300)
        manage_frame.pack()

        # ===================variables=========================
        self.username = StringVar()
        self.password = StringVar()

        lbl_username = Label(manage_frame, text="Username:", bg="crimson", fg="white", font=('arial', 15, "bold"))
        lbl_username.grid(row=1, column=0, pady=2, padx=2, sticky="w")
        txt_username = Entry(manage_frame, textvariable=self.username, font=("arial", 15, "bold"), bd=5,
                             relief=GROOVE)
        txt_username.grid(row=1, column=1, pady=2, padx=2, sticky="w")

        lbl_password = Label(manage_frame, text="Password :", bg="crimson", fg="white", font=('arial', 15, "bold"))
        lbl_password.grid(row=2, column=0, pady=2, padx=2, sticky="w")
        txt_password = Entry(manage_frame, textvariable=self.password, font=('arial', 15, "bold"), bd=5,
                             relief=GROOVE)
        txt_password.grid(row=2, column=1, pady=2, padx=2, sticky="w")
        logo = PhotoImage(file="ticky.gif")

        # =======================Button========================

        self.btnLogin = Button(manage_frame, text='Login', width=15, font=('arial', 15, 'bold'),
                               command=self.login_system)
        self.btnLogin.grid(row=3, column=0)

        btn_reset = Button(manage_frame, text='Reset', width=15, font=('arial', 15, 'bold'), command=self.clear)
        btn_reset.grid(row=3, column=1)

        btn_exit = Button(manage_frame, text='Exit', width=15, font=('arial', 15, 'bold'), command=self.iexit)
        btn_exit.grid(row=3, column=2)

        # logo = PhotoImage(file="ticky.gif")

        # logo = PhotoImage(file="whitebox.gif")

    def login_system(self):
        user = (self.username.get())
        pas = (self.password.get())

        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All Fields are required!!!")
        elif (user == str('admin')) and (pas == str(123)):
            self.navigate('home_page')
        else:
            messagebox.showinfo("Info", "check the fields and try again")

    def clear(self):
        self.username.set("")
        self.password.set("")

    def iexit(self):
        iexit = tkinter.messagebox.askyesno("Student management system", "confirm if you want to exit")
        if iexit > 0:
            self.destroy()
            return

    def __navigate(self):
        self.navigate('home_page')


# ==============================================Home Page=======================================
class HomePage(tknav.Page):

    def __init__(self, parent):
        tknav.Page.__init__(self, parent, 'home_page')

        tk.Label(self, text='Page Two').pack()
        tk.Button(self, text='Navigate to Page One', command=lambda: self.handleClick()).pack()

        title = Label(self, text="Home Page", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow",
                      fg="red").pack(side=TOP, fill=X)

    def handleClick(self):
        self.navigate('login_page')


# ================================================Login Page======================================
class RegisterPage(tknav.Page):

    def __init__(self, parent):
        tknav.Page.__init__(self, parent, 'register_page')

        tk.Label(self, text='Page Two').pack()

        tk.Button(self, text='Navigate to Page One', command=lambda: self.navigate('login_page')).pack()

        title = Label(self, text="Register Page", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow",
                      fg="red").pack(side=TOP, fill=X)

    def handleClick(self):
        self.navigate('login_page')


if __name__ == '__main__':
    App().mainloop()
