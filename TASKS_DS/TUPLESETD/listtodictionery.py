"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
14. Create a dictionary from two lists (one list of keys and one list of values)."""
list1=["supin","raju","vipin","ganesh","lakshmi"]
marks=[25,24,20,18,22]
new_dic={list1[i]:marks[i] for i in range(len(list1))}
print(new_dic)
#metod 2
new_dictionery=dict(zip(list1,marks))
print(new_dictionery)