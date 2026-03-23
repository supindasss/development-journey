"""TASK 22 || Python Collections || 24-02-2026
6. Reverse a given list without using reverse() method."""
list1=["varma","narayana","surya","das","supin"]
revrsed=[]
for i in range(len(list1)-1,-1,-1):
    revrsed.append(list1[i])
print(revrsed)    