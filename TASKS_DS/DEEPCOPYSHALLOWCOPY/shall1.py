"""Task 31 || Shallow Copy & Deep Copy || 17-03-2026
1. Write a Python program to create a list and make a shallow copy of it using the copy() method."""

list=["idly","dosa","chudney"]

list2=list.copy()

list2[0]="dosa"

print("list 1=",list)
print("list 2=",list2)

