amount=int(input("Enetr the total purchased amount "))
discount=int(input("Enter the discount in %"))
deduction=amount-(amount*discount/100)
print("your total amount is ",amount,"But you can pay ",deduction)

