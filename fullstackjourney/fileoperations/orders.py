fr=open("fullstackjourney\\fileoperations\\orders.txt","r")
order_list=[]
for line in fr:
    cleared=line.rstrip("\n")
    order_list.append(cleared)
dictionary={o:order_list.count(o) for o in order_list}    
print(dictionary)