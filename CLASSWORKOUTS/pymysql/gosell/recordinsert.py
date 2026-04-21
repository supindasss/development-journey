from mysql import connector

connection=connector.connect(host="localhost",
                             user="root",
                             password="Password@123",
                             database="product_sell")

cursor=connection.cursor()

query="""

insert into vehicle (name,model,running_kilometer,fuel_type,owner_type,place,owner) values(%s,%s,%s,%s,%s,%s,%s)
"""
data=("baleno","zeta 2020",32000,"petroll","2ndowned","kollam","priya")


cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()

print("First record is inserted successfully")
