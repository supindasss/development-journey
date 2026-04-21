from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="product_sell"
)

cursor=connection.cursor()

query="select * from vehicle"

cursor.execute(query)

records=cursor.fetchall()

for row in records:

    print(row)

cursor.close()

connection.close()