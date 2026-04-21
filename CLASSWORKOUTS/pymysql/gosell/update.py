from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="product_sell"
)

cursor=connection.cursor()

query="delete  vehicle  where id=%s"

data=(3,)

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()