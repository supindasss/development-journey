"""TASK 10 || While loop || 30-01-2026
9. Write a Python program to print each digit of a number separately using a while loop."""
user=int(input("Enter number"))
while user>0:
    last=user%10
    user=user//10
    print(last)  
