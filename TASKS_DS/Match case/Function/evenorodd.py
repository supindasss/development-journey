"""Task 16 || Function || 09-02-2026
4. Write a function that takes a number and prints whether it is even or odd."""
num1=int(input("Enter number "))
def even_or_odd(num1):
    if num1%2==0:
        print("Even number")
    else:
        print("odd number")    

even_or_odd(num1)