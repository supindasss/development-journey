"""TASK 23 || List Slicing & List Comprehension || 25-02-2026
7. Using list comprehension, create a list of even numbers from 1 to 20."""
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even=[num for num in lst if num%2==0]
print(even)