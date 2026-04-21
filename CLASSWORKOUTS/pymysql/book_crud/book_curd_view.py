#class
# create>list>retrieve>update>delete
from mysql import connector

class BookListRetrieveCreateUpdateDelete:

    def __init__(self):
        try:
            self.connection=connector.connect(host="localhost",
                                          user="root",
                                          password="Password@123",
                                          database="book_db"
                                          )
            self.cursor=self.connection.cursor()

            print("database connection Ok.....")

        except Exception as e:
            print(e)

    def list(self):

        query="select * from book"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:

            for row in records:
                print(row)

        else:

            print("records not found")   

    def create(self,title=None,author=None,price=None,pulisher=None,gnere=None,year=None) :

        query="""
                insert into book(title,author,price,pulisher,gnere,year) values(%s,%s,%s,%s,%s,%s)
                """ 
        data=(title,author,price,pulisher,gnere,year) 

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record inserted ") 
    def retrive(self,id=None):
        query="select author from book where id=%s"

        data=(id,)    

        self.cursor.execute(query,data)

        records=self.cursor.fetchall()

        if records:

            for k in records:
                print(k)

        else:

            print("its not found")    

    def delete(self,id=None):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit() 
        print("Record delted sucessfully") 

    def update(self,id=None,**kwargs) :

        place_holder=""

        for k in kwargs.keys():
            place_holder+=k+"="+"%s"+"," # placeholder+=f"{k}=%s,"

        place_holder=place_holder.rstrip(",")

        query=f"update book set {place_holder} where id = {id}"  

        data=[v for v in kwargs.values()] 

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record updated sucessfully")

book_instance = BookListRetrieveCreateUpdateDelete()
#book_instance.create(title="amoom",author="t",price=5850,pulisher="abc",gnere="novel",year="197")
#book_instance.retrive(id=1)

#book_instance.delete(id=1)
#


book_instance.update(id=4,price=700)
#book_instance.retrive(id=4)
book_instance.list()