shop_stock={"bike":120000 ,"car":300000,"traveller":1500000,"rollsroyce":10000000 }
user_input=input("What Vehicle price Do you want to check ??")
if user_input in shop_stock:
    print("The total amount of the specific vehicle is",shop_stock[user_input])
else:
    print("the specific item not in the list ")
    user_in=input("Do you want to add .....?")
    if user_in.lower()=="yes":
        value=int(input("how much money for this item.....?"))
        shop_stock[user_input]=value
        print("after appending the new element in the dictionary is ",shop_stock)
    else:
        print("Okay bye Visit again")    