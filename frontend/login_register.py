from fileinput import filename
from functools import partial
from tkinter import *

exec(open('./backend/functions.py').read())
#from functions import * 

import mysql.connector


dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="I am lonely@1",
database ="yummy"
)

db = dataBase.cursor()

def Alert(n):
    if(n == 0):
        def retrylogin():
            loginError.destroy()
            LoginPage()
        loginError = Tk()
        loginError.geometry('360x360')
        loginError.title('LOGIN ERROR!!!')
        Label(loginError, text='ERROR\nCan\'t log you in please try again').pack(side=CENTER)
        Button(loginError, text='Retry Login', command=retrylogin).pack(side=CENTER)
        loginError.mainloop()
    elif(n == 1):
        def retryregister():
            registerError.destroy()
            RegisterPage()
        registerError = Tk()
        registerError.geometry('360x360')
        registerError.title('REGISTER ERROR!!!')
        Label(registerError, text='ERROR\nCan\'t register please try again').pack(side=CENTER)
        Button(registerError, text='Retry Register', command=retryregister).pack(side=CENTER)
        registerError.mainloop()

def LoginPage():

    def validateLogin(usrnm, pswd):
        checkl = login(usrnm.get(), pswd.get())
        print("USERNAME: ", usrnm.get())
        print("PASSWORD: ", pswd.get())
        if(checkl):
            print("LOGINED SCREEN")
        else:
            Alert(0)
    
    def Register():
        login.destroy()
        RegisterPage()

    login = Tk()
    login.geometry("960x480")
    login.title('Login')
    topbar = Frame(login)
    topbar.pack(side = 'top')
    Label(topbar, text='Yummy |').pack(side='left')
    Button(topbar, text='Register', command= Register).pack(side='right')
    Label(topbar, text='| New user? -->').pack(side='right')

    body = Frame(login).pack()

    Label(body, text='\nPLEASE LOGIN').pack()
    usrnm = StringVar()
    pswd = StringVar()
    Label(body, text='\nUser Name:').pack()
    usrnmEntry = Entry(body, textvariable=usrnm).pack()
    Label(body, text='\nPassword:').pack()
    pswdEntry = Entry(body, textvariable=pswd, show='$').pack()

    validateLogin = partial(validateLogin, usrnmEntry, pswdEntry)

    Label(body,text='\n').pack()
    Button(body, text = 'Login', command=validateLogin).pack()


    login.mainloop()

def RegisterPage():

    def validateRegistration(data):
        checkr = register(data)
        if(checkr):
            LoginPage()
        else:
            Alert(1)

    def Login():
        register.destroy()
        LoginPage()

    register = Tk()
    register.geometry("960x480")
    register.title('Register')


    topbar = Frame(register)
    topbar.pack(side='top')
    Label(topbar, text='Yummy |').pack(side='left')
    Button(topbar, text='Login',command=Login).pack(side='right')
    Label(topbar, text='| Existing user? -->').pack(side='right')

    body = Frame(register).pack()

    usrnm = StringVar()
    rlnm = StringVar()
    email = StringVar()
    phno = StringVar()
    addr = StringVar()
    psswd = StringVar()
    #confpsswd = StringVar()

    Label(body, text='\nUser Name:').pack()
    pswdEntry = Entry(body, textvariable=usrnm, show='$').pack()

    Label(body, text='\nReal Name:').pack()
    pswdEntry = Entry(body, textvariable=rlnm, show='$').pack()

    Label(body, text='\nEmail Address:').pack()
    pswdEntry = Entry(body, textvariable=email, show='$').pack()

    Label(body, text='\nPhone Number:').pack()
    pswdEntry = Entry(body, textvariable=phno, show='$').pack()

    Label(body, text='\nAddress:').pack()
    pswdEntry = Entry(body, textvariable=addr, show='$').pack()

    Label(body, text='\nPassword:').pack()
    pswdEntry = Entry(body, textvariable=psswd, show='$').pack()

    data = (usrnm.get(), rlnm.get(), email.get(), phno.get(), addr.get(), psswd.get())
    #Label(body, text='\nConfirm Password:').pack()
    #pswdEntry = Entry(body, textvariable=confpsswd, show='$').pack()

    Label(body,text='\n').pack()
    Button(body, text='Create Account', command=validateRegistration).pack()
    register.mainloop()

LoginPage()


