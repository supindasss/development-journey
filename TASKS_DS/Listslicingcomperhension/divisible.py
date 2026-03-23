"""TASK 23 || List Slicing & List Comprehension || 25-02-2026
10. Create a list of numbers from 1 to 30 and use list comprehension to create a new list containing numbers divisible by 3 and 5."""
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
divisible=[num for num in lst if num%3==0 and num%5==0]
print(divisible)