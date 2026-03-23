"""Task 19 || List & List Method || 19-02-2026
12. Given a list of numbers [5, 12, 7, 20, 3, 18], create a new list that contains only the numbers greater than 10."""
list=[5, 12, 7, 20, 3, 18]
N_list=[]
for i in range(1,len(list)):
    if list[i]>10:
        N_list.append(list[i])
print(N_list)        
