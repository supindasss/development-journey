fr=open("CLASSWORKOUTS\\filedictreader\\employee.txt","r")

employees=[]

for line in fr:

    data=line.rstrip("\n").rsplit(",")

    emp={"id":data[0],"name":data[1],"posiion":data[2],"salary":data[3]}

    employees.append(emp)
    
all_employees=[e.get("name") for e in employees]

print(all_employees)

max_salary=max(employees,key=lambda c:c.get("salary"))

print(max_salary)


