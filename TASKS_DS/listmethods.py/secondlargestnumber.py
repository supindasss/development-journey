"""Task 19 || List & List Method || 19-02-2026
13. Find the second largest number in the list: [10, 45, 23, 89, 67, 89, 34]"""
lst=[10, 45, 23, 89, 67, 89, 34]
list_set=list(set(lst))
list_set.sort()
print(list_set[-2],"is the second largest number")


