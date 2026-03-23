list1=[10,11,12,13,14]
list2=[8,11,14,15,16]
#res=list(set(list1).intersection(set(list2)))
#print(res)
list1.sort()
list2.sort()
p1=0
p2=0
while(p1<len(list1) and p2<len(list2)):
    if list1[p1]==list2[p2]:
        print(list1[p1])
        p1+=1
        p2+=1
    elif list1[p1]<list2[p2]:
        p1+=1
    else:
        p2+=1

