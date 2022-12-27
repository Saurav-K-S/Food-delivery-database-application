from fileinput import filename
from functools import partial
from tkinter import *


def LoginPage():
    def validateLogin(usrnm, pswd):
        print("USERNAME: ", usrnm.get())
        print("PASSWORD: ", pswd.get())
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
    confpsswd = StringVar()

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

    Label(body, text='\nConfirm Password:').pack()
    pswdEntry = Entry(body, textvariable=confpsswd, show='$').pack()

    Label(body,text='\n').pack()
    Button(body, text='Create Account').pack()
    register.mainloop()

LoginPage()