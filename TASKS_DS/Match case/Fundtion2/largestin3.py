"""Task 17 || Function || 10-02-2026
6. Write a function that takes three numbers as parameters and returns the largest number."""
def largest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
n1,n2,n3=map(int,input("Enter the three numbers").split())
print(f"The Largest numbe is{largest(n1,n2,n3)}")   