"""TASK 09 || while loop || 29-01-2026
8. Write a program to check whether a given number is a palindrome using a while loop."""
num=int(input("Enter the number "))
rev=0
temp=num
while num>0:
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
if temp==rev:
    print(temp,"Its palindrom")    
else:
    print("Not palindrom")    