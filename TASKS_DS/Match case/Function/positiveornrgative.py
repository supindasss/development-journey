"""Task 16 || Function || 09-02-2026
7. Write a function that takes a number and prints "Positive" or "Negative"."""
number=int(input("Enter a number"))
def positive_negative(number):
    if number>0:
        print(number,"its positive")
    else:
        print(number,"is negative ")    
positive_negative(number)     


