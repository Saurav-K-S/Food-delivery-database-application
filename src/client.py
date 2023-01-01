from fileinput import filename
from functools import partial
from tkinter import *
import tkinter.ttk as ttk

from server import *

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
        loginError = Tk()
        loginError.geometry('260x60')
        loginError.title('LOGIN ERROR!!!')
        Label(loginError, text='ERROR\nCan\'t log you in please try again').pack()
        
        loginError.mainloop()
    elif(n == 1):
        registerError = Tk()
        registerError.geometry('260x60')
        registerError.title('REGISTER ERROR!!!')
        Label(registerError, text='ERROR\nCan\'t register please try again').pack()
        registerError.mainloop()

    elif(n==2):
        Error = Tk()
        Error.geometry('260x60')
        Error.title('ERROR!!!')
        Label(Error, text='ERROR\nplease try again').pack()
        Error.mainloop()

def LoginPage():

    def validateLogin(usrnm, pswd):
        print(usrnm.get())
        print(pswd.get())
        checkl = loginFN(usrnm.get(), pswd.get())
        if checkl==False:
            Alert(0)
        else:
            login.destroy()
            HomePage(checkl)
    
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
        if checkr==False:
            Alert(1)
        else:
            register.destroy()
            LoginPage()

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

# LoginPage()




def HistoryPage(data):


    def Home():
        history.destroy()
        HomePage(data)
    
    def GoBack():
        history.destroy()
        LoginPage()

    history = Tk()
    history.title("History")
    history.geometry("960x480")

    # Create the table frame and add it to the main window

    topbar = Frame(history)
    topbar.pack(side = 'top')
    Label(topbar, text='Yummy |').pack(side='left')
    Button(topbar, text='Home', command= Home).pack(side='right')
    Button(topbar, text='Login', command= GoBack).pack(side='right')

    table_frame = Frame(history)
    table_frame.pack(fill="both", expand=True)

    # Create the table header
    header = Label(table_frame, text="History", font=("Arial", 16))
    header.pack()

    # Create a scrollbar and add it to the table frame
    scrollbar = Scrollbar(table_frame)
    scrollbar.pack(side="right", fill="y")

    # Create a Treeview widget and add it to the table frame
    treeview = ttk.Treeview(table_frame, yscrollcommand=scrollbar.set, show="headings")
    treeview.pack(side="left", fill="both", expand=True)

    # Set the scrollbar to control the Treeview widget
    scrollbar.config(command=treeview.yview)

    id = data.get("id")
    values = historyFN(id)

    # Add the column headings to the Treeview widget
    treeview["columns"] = ("col1", "col2", "col3","col4")
    treeview.column("col1", width=100)
    treeview.column("col2", width=100)
    treeview.column("col3", width=100)
    treeview.column("col4", width=100)
    treeview.heading("col1", text="Item")
    treeview.heading("col2", text="Total Price")
    treeview.heading("col3", text="Units")
    treeview.heading("col4", text="Hotel")

    # Add the values to the Treeview widget
    if values!=None:
        for i, value in enumerate(values):
            treeview.insert("", "end", text="i+1", values=value)

    # Run the Tkinter event loop
    history.mainloop()




def HomePage(data):
    def History():
        home.destroy()
        HistoryPage(data)

    def GoBack():
        home.destroy()
        LoginPage()
    

    def button_click(text1, text2):
        # Do something with the text in the text boxes
        print(text1.get())
        print(text2.get())
        print(data)
        units = int(text2.get())
        item_id = int(text1.get())
        check = add_itemFN(units,data.get("id"),item_id)
        if check==False:
            Alert(2)
        else:
            home.destroy()
            HomePage(data)

    # Create the main window
    home = Tk()
    home.title("Home")
    home.geometry("960x480")

    topbar = Frame(home)
    topbar.pack(side = 'top')
    Label(topbar, text='Yummy |').pack(side='left')
    Button(topbar, text='History', command= History).pack(side='right')
    Button(topbar, text='Login', command= GoBack).pack(side='right')
    

    # Create a frame to hold the text boxes and button
    frame = Frame(home,width=960,height=400)
    frame.pack()
    header = Label(frame, text="Home", font=("Arial", 16))
    header.pack()

    # Create a scrollbar and add it to the table frame
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # Create a Treeview widget and add it to the table frame
    treeview = ttk.Treeview(frame, yscrollcommand=scrollbar.set, show="headings")
    treeview.pack(side="left", fill="both", expand=True)

    # Set the scrollbar to control the Treeview widget
    scrollbar.config(command=treeview.yview)


    values = fetch_itemsFN()

    # Add the column headings to the Treeview widget
    treeview["columns"] = ("col1", "col2", "col3","col4")
    treeview.column("col1", width=100)
    treeview.column("col2", width=100)
    treeview.column("col3", width=100)
    treeview.column("col4", width=100)
    treeview.heading("col1", text="Item_id")
    treeview.heading("col2", text="Name")
    treeview.heading("col3", text="Price")
    treeview.heading("col4", text="Units Available")

    # Add the values to the Treeview widget
    if values!=None:
        for i, value in enumerate(values):
            treeview.insert("", "end", text="i+1", values=value)

    # Create the text boxes
    text1 = StringVar()
    textbox1 = Entry(frame, textvariable=text1)
    textbox1.pack(side="left")

    text2 = StringVar()
    textbox2 = Entry(frame, textvariable=text2)
    textbox2.pack(side="left")


    # Create the button
    button = Button(frame, text="Buy Item!", command=lambda: button_click(text1, text2))
    button.pack(side="left")

    # Run the Tkinter event loop
    home.mainloop()



LoginPage()