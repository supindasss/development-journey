"""Task 17 || Function || 10-02-2026
4. Write a function that takes a number as a parameter and prints whether it is even or odd."""
def even_odd(number):
    if number%2==0:
        print(f"{number}is even number ")
    else:
        print(f"{number} is odd number")    
number=int(input("Enter number"))        
even_odd(number)