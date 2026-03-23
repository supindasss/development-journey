"""TASK 09 || while loop || 29-01-2026
6. Write a program to count the number of digits in a given number using a while loop."""
user=int(input("Enter the number "))
count=0
if user==0:
    count=1
else:
    while user>0:
        user=user//10
        count=count+1
print("Total number of digits is",count)   


 
    
