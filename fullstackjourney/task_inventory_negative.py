Available_stock=100
keep_shoping=True
while True:
   user_input=int(input("How many quantitys do you want ??"))
   if user_input<0 :
      print("Nice try ...you cant trick me")
   elif user_input<=Available_stock:
        Available_stock=Available_stock-user_input
        print("Thank you for using Your order is placed ,balance stock in store is ",Available_stock) 
   else :
        print("You cant place this order because the available stock is only",Available_stock)
   keep_shoping=input(" Do you want to stop ??")
   if keep_shoping.lower()=="yes":
    print("see you next time bye!!!")
    break

         
    
       