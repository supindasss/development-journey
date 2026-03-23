"""Task 25 || Lambda Function || 02-03-2026
7. Write a program to read the entire content of a file and display it."""
op=open("TASKS_DS\\Fileoperations\\ready.txt","r")
lst=[]
for lang in op:
    cleane=lang.rstrip("\n")
    lst.append(cleane)
print(lst)    
