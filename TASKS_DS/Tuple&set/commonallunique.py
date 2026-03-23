"""Task 20 ||  Tuple & Set || 20-02-2026
7. Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, write a program to find:
* Common elements
* All unique elements from both sets"""
set1={1, 2, 3, 4} 
set2={3, 4, 5, 6}
print(f"{set1.union(set2)} ALL UNIQUE ELEMENTS")
print(f"{set1.intersection(set2)} ALL COMMON ELEMENTS")