"""TASK-04 || if else,if elif else 
7. Write a Python program to check whether a given year is a leap year
"""
year=int(input("Enter a year"))
if(year%400==0)or(year%4==0):
    print("Leap year")
else:
    print("Not a leap year") 
       