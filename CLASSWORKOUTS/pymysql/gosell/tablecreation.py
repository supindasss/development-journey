from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="product_sel"
)
cursor=connection.cursor()

query="""create table vehicle(id int auto_increment primary key,
                              name varchar(200) not null ,
                              model varchar(200) not null ,
                              running_kilometer int default 50,
                              fuel_type enum("diesel","petroll") default "petroll" ,
                              owner_type enum("single","2ndowned","thirdowned") default "single" ,
                              place varchar(200) not null ,
                              owner varchar(200) not null);
                              """

cursor.execute(query)

connection.commit()

cursor.close()

connection.commit()

print("the table has been created sucessfully")