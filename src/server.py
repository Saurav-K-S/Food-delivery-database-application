

import mysql.connector


dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="101101101101",
database ="yummy"
)

db = dataBase.cursor()



def loginFN(user,pwd):

    try:

        find_user_query="select * from user where id=%s and password=%s"
        adr = (user,pwd)
        db.execute(find_user_query,adr)
        user  = db.fetchone()

        if user==None:
            return False
        else:
            return {"id":user[0],"name":user[1],"email":user[2],"Phone":user[3],"Address":user[4],"role":user[5]}
        
    except mysql.connector.Error as err:
        print(err)
        return "Unexpected Error Occurred"

def registerFN(data):
    try:

        add_user_query="insert into user values(%s,%s,%s,%s,%s,%s,%s)"
        adr = (data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        db.execute(add_user_query,adr)
        dataBase.commit()
        return True

    except mysql.connector.Error as err:
        print(err)
        return False


def add_itemFN(purchased_units,customer_id,item_id):
    try:

        find_hotel_id_query="select * from item where id=%s"
        adr=(int(item_id),)
        db.execute(find_hotel_id_query,adr)
        data=db.fetchone()

        if data!=None:
            item_id = data[0]
            name = data[1]
            price = int(data[2])
            units = int(data[3])
            hotel_id = data[4]

            if units<purchased_units:
                return False

            total_price = price*int(purchased_units)

            add_item_query="insert into ordered_item (name,total_price,unit,hotel_id,customer_id)values(%s,%s,%s,%s,%s)"
            adr = (name,total_price,purchased_units,hotel_id,customer_id)
            db.execute(add_item_query,adr)
            dataBase.commit()

            remaining_unit = units-purchased_units
            update_item_query="update item set unit=%s  where id =%s"
            adr = (remaining_unit,item_id)
            db.execute(update_item_query,adr)
            dataBase.commit()
            return True
        
        elif data==None:
            return False

    except mysql.connector.Error as err:
        print(err)
        return False
    


def fetch_itemsFN():
    try:

        all_items_query="select item.*,user.name from item , user where item.hotel_id=user.id and unit!=0"
        db.execute(all_items_query)
        items = db.fetchall()
        return items

    except mysql.connector.Error as err:
        print(err)
        return False
    


def historyFN(user_id):
    try:

        ordered_items_query="select S.name, S.total_price,S.unit ,hotel.name from ordered_item as S,user as hotel where S.hotel_id = hotel.id and S.customer_id=%s"
        adr=(user_id,)
        db.execute(ordered_items_query,adr)
        items = db.fetchall()
        if items!=None:
            return items
        else:
            return None
    except mysql.connector.Error as err:
        print(err)
        return False
    

# a=history("cj@1234")
# print(a)


#registerFN(("cj@1234","Vyshnav C J","cj2@gmail.com","9846054605","8 mile, pampady P O, Pin-code 682301","123456","customer"))


# add_item(("chicken curry","150","2"),"plaza@123","cj@123","1")


# history("cj@123")

