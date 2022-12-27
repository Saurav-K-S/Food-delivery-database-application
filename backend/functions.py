

import mysql.connector


dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="I am lonely@1",
database ="yummy"
)

db = dataBase.cursor()



def login(user,pwd):

    try:

        find_user_query="select * from user where id=%s and password=%s"
        adr = (user,pwd)
        db.execute(find_user_query,adr)
        user  = db.fetchone()

        if user==None:
            return "Invalid Credentials"
        else:
            return {"id":user[0],"name":user[1],"email":user[2],"Phone":user[3],"Address":user[4],"role":user[5]}
        
    except mysql.connector.Error as err:
        print(err)
        return "Unexpected Error Occurred"

def register(data):
    try:

        add_user_query="insert into user values(%s,%s,%s,%s,%s,%s,%s)"
        adr = (data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        db.execute(add_user_query,adr)
        dataBase.commit()
        return True

    except mysql.connector.Error as err:
        print(err)
        return False


def add_item(data,hotel_id):
    try:

        add_item_query="insert into item (name,price,unit,hotel_id)values(%s,%s,%s,%s)"
        adr = (data[0],data[1],data[2],hotel_id)
        db.execute(add_item_query,adr)
        dataBase.commit()
        return True

    except mysql.connector.Error as err:
        print(err)
        return False
    


def update_item(data,hotel_id,item_id):
    try:

        add_item_query="update item set price=%s,unit=%s  where id =%s and hotel_id=%s"
        adr = (data[0],data[1],item_id,hotel_id)
        db.execute(add_item_query,adr)
        dataBase.commit()
        return True

    except mysql.connector.Error as err:
        print(err)
        return False



# success = register(("cj@123","Vyshnav","cj@gmail.com","7306255230","TKS Road, Maradu P O, Pincode 682304","123456","customer"))

# print(success)

# role = login("domi123","123456")

# print(role)

# success = add_item(("Rice","30","10"),"domi123")

# print(success) 

# success = update_item(("32","20"),"domi123","1")

# print(success) 