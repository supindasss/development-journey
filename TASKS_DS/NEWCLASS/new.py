"""dictionary methods
def keys():return all keys
def values():return all values from the dictionary
def items():return all keys and values
def get(key."print this message if the key is not presented in the dictionary "):for returning specific key value 
def pop(seff,key):this method is used to remove a specific key value pair,and prints removed key value  

"""


employee={
    "dijo":300,
    "akshay":1000,
    "edwin":800,
    "alan":15000,
    "manoj":0,
    "supin":0,
    "sreeyesh":500}
#for keys in employee.keys():
    #print(keys)
#for values in employee.values():
    #print(values)    
#for k,v in employee.items():
    #print(k,v)  
#print(employee.get("Name"))    
#print(employee.get("emial","dummy@gmail.com")) 
#employee.pop("Name")
#print(employee)
#employee["bonus"]=20000
#employee["salary"]+=10000
#print(employee)
t_expense=0
for v in employee.values():
    t_expense+=v

print("Total Expense",t_expense)   
nw=t_expense/len(employee)
print(nw)

neww={}
for k,v in employee.items():
    payment=nw-v
    neww[k]=payment
print(neww)    
