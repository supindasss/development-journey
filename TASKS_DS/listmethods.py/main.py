"""Task 19 || List & List Method || 19-02-2026
15. Given the list [2, 4, 6, 8, 10], create a new list where each element is multiplied by 3."""
o_list=[2, 4, 6, 8, 10]
N_list=[]
for i in range(0,len(o_list)):
    multi=o_list[i]*3
    N_list.append(multi)
print(N_list)
