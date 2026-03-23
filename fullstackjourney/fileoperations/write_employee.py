employees=["supin","surya","narayanan","varma","unni"]

fw=open("fullstackjourney\\fileoperations\\employees.txt","w")

for e in employees:
    fw.write(e+"\n")
print("completed")    