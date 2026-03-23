"""TASK 09 || while loop || 29-01-2026
5. Write a Python program to print the multiplication table of a given number using a while loop."""
user=int(input("Enter the number to get its mutiplication table"))
i=1
while i<=10:
    print(i,"X",user,"=",i*user)
    i+=1
    