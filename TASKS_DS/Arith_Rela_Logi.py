""" TASK 3 -ARITHMATIC  || RELATIONAL || LOGICAL OPERATORS 21-01-2026||
10.Read Two numbers and print the result of num1>0 or num2>0
"""
keep_going=True
while True:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
    print(num1>0 or num2>0)
    keep_going=input("Stop ???")
    if keep_going.lower()=="yes":
        keep_going=False
        break











