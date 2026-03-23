Shop_store={"Chips":20 ,"soda":15,"water":20,"Tea":10}
for item,price in Shop_store.items():
    print(item,"price:",price)
keep_shoping=True
while True:

 user=input("Enetr the item would  like to have ")    
 if user in Shop_store :
    qty=int(input("Enter how many qnty do you want "))
    if qty<0 :
        print("You cant trick me ")
        keep_shoping=input("want to continue....")
        if keep_shoping.lower()=="no":
            keep_shoping=False
            print("See you on the other side ......Bye Bye ")
            break

    elif qty>10:
        print("its covid 19 right now....you cant purchase more than 10 ok")
    else:
        pricee=qty*Shop_store[user]
        print("Your Total amount is ",pricee)
        con=input("Do you wish to continue on that amount ??")
        if con.lower()=="yes":
            print("Your payment is completed ......Enjoy youy meal ")
            keep_shoping=input("Want to stop???")
            if keep_shoping.lower()=="yes":
                keep_shoping=False
                break
        else:
            print("GET OUT")

 else:
    print("sorry that specific item is not in available ")
    add=input("would you like to add ??     (yes/no)")
    if add.lower()=="yes":
        value=int(input("Enter the price for the new item "))
        if value<0:
            print("GO Go no way")
        else: 
            print("adding this item")
            Shop_store[user]=value
            print("after updating the list is ",Shop_store)
    else:
        print("You priffered no so see you next time !!!")
        


