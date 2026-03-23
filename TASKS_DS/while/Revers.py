"""TASK 09 || while loop || 29-01-2026
7. Write a Python program to reverse a number using a while loop."""
num=int(input("Enter the number to find its revers "))
rev=0
if num==0:
    print("0")
else:
    while num>0:
        digit=num%10
        rev=(rev*10)+digit 
        num=num//10

    print("The reverse order is",rev)       