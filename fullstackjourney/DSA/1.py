"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6"""

"""list=[1,2,3,5]
length=len(list)
for i in range(1,length+1):
    if i not in list:
        print(i,"is the missing one ")  
        break"""
"""list=[2,3,4,5]
length=len(list)
for i in range(length,0,-1):
    if i not in list:
        print(i,"is the missing")"""
"""lst=[1,2,3,4,5]
length=len(lst)
for i in range(1,length+2):
    if i not in lst:
        print(i,"is the missing one ")"""
def missingleastpositive(arr):
    arr.sort()
    prev=0
    next=prev+1
    while(prev<=len(arr)-2):
        difference=arr[next]-arr[prev]  
        if difference!=1:
            print(arr[prev]+1,"is the missing number") 
            break
        prev+=1
        next=prev+1 
    else:
        print(arr[-1]+1)       

missingleastpositive([1,2,3,4])