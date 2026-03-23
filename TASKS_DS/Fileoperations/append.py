"""Task 25 || Lambda Function || 02-03-2026
9. Write a program to append new content to an existing file without deleting old data."""
appending=open("TASKS_DS\\Fileoperations\\appending.txt","a")
lst=["gireesh","nitheesh","sudheesh","dineesh","hashirkka"]
for name in lst:
    appending.write(name+"\n")
print("the operation is completed!!!")    
