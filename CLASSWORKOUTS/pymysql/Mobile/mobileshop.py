#CRUD==>[id,title,brand,specs,price]
from mysql import connector

class MobileCreateRetriveListDelete:

    def __init__(self):
        
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="mobileshop"
            )

            self.cursor=self.connection.cursor()

            print("database connection is ok !!!")  
        except Exception as e:

            print(e)    

    def list(self):
        query="select * from mobile"

        self.cursor.execute(query)

        result=self.cursor.fetchall()

        if result:

            for r in result:

                print(r)
        else:

            print("Record is not found")         
    
    def create(self,title,brand,specs,price):

        query="insert into mobile(title,brand,specs,price) values(%s,%s,%s,%s)"

        data=(title,brand,specs,price)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record inserted ")

    def retrive(self,id=None):

        query="select * from mobile where id=%s"

        data=(id,) 

        self.cursor.execute(query,data)

        records=self.cursor.fetchall()

        print("the selected record is")

        if records:

            for r in records:

                print(r)

        else:

            print("Invalid, check the id again and tryagain")  

    def delete(self,id=None):

        query="delete from mobile where id=%s"

        data=(id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("the sepcific record is deleted sucessfully")              


mobile_instance=MobileCreateRetriveListDelete()

#mobile_instance.create(title="IPHONE 16",brand="apple",specs="Less lag",price=150000)
mobile_instance.list()

mobile_instance.retrive(id=2)

mobile_instance.delete(id=5)

print("the record after deletion is ")

mobile_instance.list()

