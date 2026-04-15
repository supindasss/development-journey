"""Task 31 || Shallow Copy & Deep Copy || 17-03-2026
2. Write a program to demonstrate shallow copy using the copy module."""

import copy

original_list = [0,1,2,3,4,5,6]

copied_list = copy.copy(original_list)

copied_list.append(7)

print("original list : ",original_list)

print("copied list : ",copied_list)