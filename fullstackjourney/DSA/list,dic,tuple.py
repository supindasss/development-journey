# find duplicate numbers without using any predefined methods
def find_duplicates(arr):
    arr.sort()
    new_list=set()
    prev=0
    next=prev+1
    while(prev<=len(arr)-2):
        difference=arr[next]-arr[prev]
        if difference==0:
            new_list.add(arr[prev])
        prev+=1
        next=prev+1
    print(new_list) 
find_duplicates([11,12,13,13,15,15,15,18,18,15,14,13])           