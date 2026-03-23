my_stock=["Apple","Orange","Pinapple","banana","Milk"]
print("The predefined list is",my_stock)
keep_going=True
while True:
 chose_option=int(input("Enter Operation to select Add Or Remove "))
 if chose_option==1:
   print("!!!!!!!!!!!!!!!!!!!!You are in Addition Menue!!!!!!!!!!!!!!!!!!")
   Add_item=input("Enetr a number or string To add item on the predifined list")
   if Add_item in my_stock :
      print("The Item is alredy in the list you cant add this on the existing list ")
      keep_going=input("Do you want to continue")
      if keep_going.lower()=="no":
         keep_going=False
         break       
   else:   
     my_stock.append(Add_item)
     print("The updated list after addition is",my_stock)
 elif chose_option==2:
   print("!!!!!!!!!!!!!!!!! You are in remove menue!!!!!!!!!!!!!!!!!!!!!!!")
   remove_item=input("Enter the string to remove from existing list")
   if remove_item in my_stock:
      print("You are remmove that item")
      my_stock.remove(remove_item)
      print("The list after removing the item is",my_stock)
      keep_going=input("You want to stop")
      if keep_going.lower()=="yes":
        keep_going=False
        break
   else:
      print("The item is not in the list ")   
      

      


