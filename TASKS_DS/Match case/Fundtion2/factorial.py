"""Task 17 || Function || 10-02-2026
7. Write a function that takes a number as a parameter and returns the factorial of that number."""
def factorial(number):
    fact=1
    for number in range(1,number+1):
        fact=fact*number
        number=number-1
    print(fact)
number=int(input("eneter number "))        
factorial(number)    