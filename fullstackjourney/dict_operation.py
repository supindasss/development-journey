prices={"Apple":120, "orange":130,"pinapple":140,"watermelon":150}
print("the dictionary before doing any operation is ",prices)
prices.pop("orange")
print("after doing the operation in the dictionary is ",prices)

for item,price in prices.items():
    print("item:",item,"price is",price)
   
