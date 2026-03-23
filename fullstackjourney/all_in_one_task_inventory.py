""" 
need to add hacker protection/input validation -tsk1
calculate the bill(price tak, total=QTY*price)-pay bill-tsk2
Selling and refilling-tsk3
Adding rule:-10(maximum limit of a one person to buy)-tsk4
Security Gate for entering -tsk5
  """
Password=input("Authorisation Required Enter the password to continue")
if Password=="supin123":
    print("**********WELCOME TO THE MAIN STORE***********")
    Buying_price=120
    selling_price=150
    available_quantity=100
    Total_Sale_Amount=0
    Total_Purchase_Amount=0
    keep_shoping=True
    while True: 
       chose_option=int(input("BUYING OR SELLING OR REPORT ANSWER RESPECTIVELY 1  2  3 "))
       if chose_option==1:
           print("Your selected Buying ")
           buying=int(input("just eneter the whole quantity in numbers "))
           TotalB_amount=buying*Buying_price
           if buying<0:
               print("You cant trick me")
               keep_shoping=input("Do you wish to stop ")
               if keep_shoping.lower()=="yes":
                   keep_shoping=False
                   break
           else: 
             print("the total amount is",TotalB_amount)  
             pay_buying=input(" Do you wish to Pay ??")
             if pay_buying.lower()=="yes":
                 available_quantity=available_quantity+buying
                 Total_Purchase_Amount=Total_Purchase_Amount+TotalB_amount
                 print("Thank you for doing bussiness with Us visit again remaining quantity in you store after purchase is",available_quantity)
                 keep_shoping=input("stop..?")
                 if keep_shoping=="yes":
                     print("Thank you visit again")
                     keep_shoping=False
                     break
             else:
                 print("you are failed to Buying ")
                 print("Your current stock is",available_quantity)
                 keep_shoping=input("do you want to stop??")
                 if keep_shoping.lower()=="yes":
                     keep_shoping=False
                     break
       elif chose_option==2:
            print("You are sellected selling menue")
            selling=int(input("Enter How many stock do you want ??"))
            if selling<0 :
                print("Cant do that visit again")
                keep_shoping=input("Stop ??")
                if keep_shoping.lower()=="yes":
                    keep_shoping=False
                    print("see you on the other side")
                    break
            elif available_quantity<selling:
                print("Sorry We can't do right now because the total available stock is only ",available_quantity)    
            elif selling>10:
                print("You cant Buy More than 10 in once ")
                keep_shoping=input("do you want to stop")
                if keep_shoping.lower()=="yes":
                   keep_shoping=False
                   break
            else :
                  Total_samount=selling*selling_price
                  print("The total amount to be paid is ",Total_samount,)
                  sell_get=input("Do you wish to continue ??")
                  if sell_get.lower()=="yes":
                      available_quantity=available_quantity-selling
                      Total_Sale_Amount=Total_Sale_Amount+Total_samount
                      print("You are selled the item, balance quantity is ",available_quantity)    
                  else:
                      keep_shoping=False
                      break
       elif chose_option==3:
           print("************************You are in Report Menue************************")   
           print("Total amount of Purchase is",Total_Purchase_Amount)
           print("Total amount of sale ",Total_Sale_Amount)
           Total_profit=Total_Sale_Amount-Total_Purchase_Amount
           print("Your bussines Total profit is",Total_profit)     
else:
    print("Password is incorrect Try after some time!!!")
    