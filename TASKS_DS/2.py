"""TASK-04 || if else,if elif else 
2. Write a Python program to check whether a given number is even or odd

"""
keep_going=True
while True:
    number=int(input("Enter the number "))
    if number<0:
        print("The given number is negative")
        keep_going=input("stop ")
        if keep_going.lower()=="yes":
            keep_going=False
            break
    elif number%2==0:
        print("The given number is even")
        keep_going=input("stop ") 
        if keep_going.lower()=="yes":
            keep_going=False
            break
    else:
        print("The number is odd")
        keep_going=input("stop ") 
        if keep_going.lower()=="yes":
            keep_going=False
            break
