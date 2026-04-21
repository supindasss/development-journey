from mysql import connector

class CreateDeleteUpdateRetrive:

    def __init__(self):
        try:
            self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="home_db"
            )

            self.cursor=self.connection.cursor()

            print("database connected sucessfully")

        except Exception as e:

            print(e)  

    def insert(self,sqft=None,bhk=None,price=None,location=None,is_available=None,note=None):

        query="insert into property(sqft,bhk,price,location,is_available,note) values(%s,%s,%s,%s,%s,%s)"
        data=(sqft,bhk,price,location,is_available,note) 

        self.cursor.execute(query,data)

        self.connection.commit()

        self.cursor.close()

        self.connection.close()

        print("Data inserted ")

    def listtable(self):

        query="select * from property"

        self.cursor.execute(query)

        result=self.cursor.fetchall()

        if result:

            for row in result:

                print(row)    
        else:

            print("the table is empty")  

    def retrive(self,id=None):

        query="select * from property where id=%s"

        data=(id,)          

        self.cursor.execute(query,data)

        result=self.cursor.fetchone()

        if result:
            print(result)

        else:
            print("invalid entry !!!")

    def delete(self,id=None):

        query="delete from property where id = %s" 

        data=(id,)           

        self.cursor.execute(query,data)

        self.connection.commit()
        
        print("the deletion from that sepcific id is completed")

    def update(self,)    


home_instance=CreateDeleteUpdateRetrive()
home_instance.listtable()
home_instance.retrive(id=5)

home_instance.delete(id=2)
home_instance.listtable()




          