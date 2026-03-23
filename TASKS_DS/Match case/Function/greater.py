"""Task 16 || Function || 09-02-2026
6. Write a function that takes two numbers and returns the greater number."""
n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
def greater(n1,n2):
    if n1>n2:
        print(n1,"is the largest")
    else:
        print(n2,"is the largest")    
greater(n1,n2)        