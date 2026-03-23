"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
7. Write a program to check whether one set is a subset of another set."""
set_a={1,2,3,4,5,6}
set_b={3,4,5}
if set_b.issubset(set_a):
    print(f"Set {set_b} is the subset of {set_a}")
else:
    print("not subset")    