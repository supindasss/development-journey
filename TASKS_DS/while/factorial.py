"""TASK 09 || while loop || 29-01-2026
10. Write a program to find the factorial of a given number using a while loop."""
num=int(input("Enter the number "))
fact=1
while num>0:
    fact=fact*num
    num=num-1

print("The factorial of given num ber is ",fact)    