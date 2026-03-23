
inventory={
    "iphones":{"Price":99400,"Stock":20,"Color":"Black"},
    "samsung":{"Price":96500,"Stock":13,"Color":"Silver"},
    "oppo":{"Price":66500,"Stock":10,"Color":"Seablue"}
}
db_pass=543210
passw=input("Enter Your Password to enter the store")
keep_going=True
while True:
    if passw==db_pass:
        print("\n______________You are logined Sucessfully____________\n")
        print("SELL\n")
        print("PURCHASE")
        print("Show Report")
        print("View ALL Stock")
        choose_option=int(input("Enter Your option "))
        if choose_option==4:

            for items,value in inventory.items(): # here items get the name key,=>iphones,samsung,oppo, : value gets inside phones 
                price=value["Price"]
                if(price<80000):
                    print(f"Models:{items}")
                    print(f"price:{value["Price"]}")
                    print("Stocks:",value["Stock"])# can also be used like this 
                    print(f"colors:{value["Color"]}")
                    print("_"*30) 
        elif choose_option==1:

            user=input("Which phone do you like ")    
            if user in inventory:
                print("The price per piece of the phone is ",inventory[user]["Price"])
                qty=int(input("Enter how many quantitys do you want??"))
                