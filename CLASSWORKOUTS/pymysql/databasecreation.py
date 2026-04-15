from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123"
)

cursor=connection.cursor()

query="create database db_py"

cursor.execute(query)

connection.commit()

print("connection is completed")
