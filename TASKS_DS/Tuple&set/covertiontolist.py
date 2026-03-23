"""Task 20 ||  Tuple & Set || 20-02-2026
4. Given a tuple (1, 2, 3, 4, 5), convert it into a list, add a new element, and convert it back to a tuple."""
tuples=(1, 2, 3, 4, 5)
list_tuple=list(tuples)
print(f"The tuple is{tuples}")
print(f"the tuple after convert to list is{list_tuple}")
list_tuple.insert(3,8)
print(f"The tuple after adding new element is{tuple(list_tuple)}")

