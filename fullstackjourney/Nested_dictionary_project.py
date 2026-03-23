mobile_galery={
    "iphone 15":{"price":125000,"stock":15,"color":"Black"},
    "samsung s24":{"price":115000,"stock":15,"color":"White",},
    "vivo x200":{"price":99400,"stock":30,"color":"Seablue"}
}
while True:
    print("--------------------MOBILE GALERY-------------------")
    print("View all Stocks")
    print("Purchase ")
    print("Sell")
    print("Report")
    print("Exit")
    user=int(input("Enter Your choice (1-4) "))
    if user==1:
        print("Viewing all stocks in your dictionary")
        print("\n")
        for item,value in mobile_galery.items():
            print(f"Models:{item}")
            print(f"price {value['price']}")
            print(f"stock {value['stock']}")
            print(f"color {value['color']}")
            print("_"*30)
    elif user==3:
        print(" You are in Selling Menue")
        Search_key=input("Which model Name Are You looking for ??")
        if Search_key in mobile_galery:
            print("This model is Available")
            print("The price per piece is",mobile_galery[Search_key]['price'],"And the Available Stock is ",mobile_galery[Search_key]['stock'])
            buy=input("Would you like Sell the preferred model")
            if buy.lower()=="yes":
                stock=int(input("Also specify number of stocks to sell??"))
                if stock<mobile_galery[Search_key]['stock']:
                    print("The total amount will be",mobile_galery[Search_key]['price']*stock)
                    cont=input("Are You Ready To sell ??")
                    if cont.lower()=="yes":
                        print("You are successfully selled the item ")
                        mobile_galery[Search_key]['stock']=mobile_galery[Search_key]['stock']-stock
                        print(mobile_galery[Search_key]['stock'])
                else:
                    print("You Cant Sell this item bcos the available stock is ",mobile_galery[Search_key]['stock'])                      
    elif user==3:
        print("Exicuting 3rd part")

    elif user==4:
        print("Exicuting 4th part ")



