"""TASK-04 || if else,if elif else 
1.Write a Python program to check whether a given number is positive or negative

"""
keep_going=True
while True:
    number=int(input("Enter a number "))
    if(number<0):
        print("The give number is negative")
        keep_going=input("Do you want to continue....?")
        if  keep_going.lower()=="no":
            keep_going=False
            break
    else:
        print("the given number is positive")
        keep_going=input("Do you want to continue....?")
        if  keep_going.lower()=="no":
            keep_going=False
            break



