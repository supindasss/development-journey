"""Task 16 || Function || 09-02-2026
8. Write a function that takes a number and returns True if it is zero, else False."""
n=int(input("Enter a number : "))
def is_zero(n):
    if n==0:
        return True
    else:
        return False
print(is_zero(n))   