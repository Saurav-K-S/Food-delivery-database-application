from fileinput import filename
from functools import partial
from tkinter import *

from functions import loginFN, registerFN

# exec(open('./backend/functions.py').read())
#from functions import * 

# import mysql.connector


# dataBase = mysql.connector.connect(
# host ="localhost",
# user ="root",
# passwd ="I am lonely@1",
# database ="yummy"
# )

# db = dataBase.cursor()

def Alert(n):
    if(n == 0):
        def retrylogin():
            loginError.destroy()
            LoginPage()
        loginError = Tk()
        loginError.geometry('360x360')
        loginError.title('LOGIN ERROR!!!')
        Label(loginError, text='ERROR\nCan\'t log you in please try again').pack()
        Button(loginError, text='Retry Login', command=retrylogin).pack()
        loginError.mainloop()
    elif(n == 1):
        def retryregister():
            registerError.destroy()
            RegisterPage()
        registerError = Tk()
        registerError.geometry('360x360')
        registerError.title('REGISTER ERROR!!!')
        Label(registerError, text='ERROR\nCan\'t register please try again').pack()
        Button(registerError, text='Retry Register', command=retryregister).pack()
        registerError.mainloop()

def LoginPage():

    def validateLogin(usrnm, pswd):
        print(usrnm.get())
        print(pswd.get())
        checkl = loginFN(usrnm.get(), pswd.get())
        print(checkl)
    
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
    
    validateLogin = partial(validateLogin, usrnm, pswd)

    Label(body,text='\n').pack()
    Button(body, text = 'Login', command=validateLogin).pack()


    login.mainloop()

def RegisterPage():

    def validateRegistration(data):
        datanew = [data[0].get(),data[1].get(),data[2].get(),data[3].get(),data[4].get(),data[5].get(),data[6]]
        print(datanew)
        checkr = registerFN(datanew)
        print(checkr)

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
    usrnmEntry = Entry(body, textvariable=usrnm).pack()

    Label(body, text='\nReal Name:').pack()
    rlnmEntry = Entry(body, textvariable=rlnm).pack()

    Label(body, text='\nEmail Address:').pack()
    emailEntry = Entry(body, textvariable=email).pack()

    Label(body, text='\nPhone Number:').pack()
    phnoEntry = Entry(body, textvariable=phno).pack()

    Label(body, text='\nAddress:').pack()
    addrEntry = Entry(body, textvariable=addr).pack()

    Label(body, text='\nPassword:').pack()
    psswdEntry = Entry(body, textvariable=psswd).pack()

    data = [usrnm, rlnm, email, phno, addr, psswd, "customer"]


    validateRegistration = partial(validateRegistration,data)
    #Label(body, text='\nConfirm Password:').pack()
    #pswdEntry = Entry(body, textvariable=confpsswd).pack()


    Label(body,text='\n').pack()
    Button(body, text='Create Account', command=validateRegistration).pack()
    register.mainloop()

LoginPage()


