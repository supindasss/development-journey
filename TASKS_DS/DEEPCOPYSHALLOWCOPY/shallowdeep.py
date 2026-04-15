"""Task 31 || Shallow Copy & Deep Copy || 17-03-2026
6. Write a program to compare shallow copy and deep copy using nested lists."""

from copy import deepcopy

food_list = [
    ["Cardamom", "Cloves", "Cinnamon"],             
    ["Onions", "Tomatoes", "Mint leaves"],   
    ["Chicken", "Mutton", "Paneer"],         
    ["Basmati Rice", "Ghee", "Saffron"]      
]

print("PERFORMING SHALLOW COPY FROM MAIN FOOD LIST")

shallow_copy=food_list[0].copy()

shallow_copy[0] = "Star Anise"
shallow_copy[1] = "Bay Leaf"
shallow_copy[2] = "Black Pepper"

deepcopy1=deepcopy(food_list)


print("ORIGINAL LIST =",food_list)
print("THIS IS THE EXAMPLE OF SHALLOW COPY here only chnages first index list \n",shallow_copy)

print("DEEP COPY ")

deepcopy1[2][0] = "Fish"
deepcopy1[2][1] = "Prawns"
deepcopy1[2][2] = "Crab"

print("ORIGINAL LIST =",food_list)
print("THIS IS THE EXAMPLE OF SHALLOW COPY here only chnages last index list \n",deepcopy1)




