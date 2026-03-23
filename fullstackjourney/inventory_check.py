current_stock=50
keep_shoping=True
while keep_shoping:
  user_quantity=input("Please Enter how many quanitys do you want ?")
  need=int(user_quantity)
  if(current_stock>=need) :
        print("your order is placed")
        current_stock=current_stock-need
        print("Available stocke is ",current_stock)
  else :
      print("Your order cannot satisfy because Available stocke is ",current_stock)
    
  keep_shoping=input("Do you want to Stop....?")
  if keep_shoping=="YES" or keep_shoping=="yes":
   keep_shoping=False