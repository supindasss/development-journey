amount=int(input("Enter the total MRP Price"))
dis=25
if amount>=1000 :
   dis_amount= amount-(amount*dis/100)
   print("Your actual amount is",amount,"but you can pay only",dis_amount)
else :
   print("Sorry You are not applicable for discount !!!! PAY the amount",amount,"  ")   
