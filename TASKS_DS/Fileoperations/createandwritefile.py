"""Task 25 || Lambda Function || 02-03-2026
6. Write a Python program to create a file and write 5 lines of text into it."""
file=open("TASKS_DS\\Fileoperations\\createandwritefile.txt","w")
list=["apple","orange","piapple","grapes"]
for fruits in list:
    file.write(fruits+"\n") #only strings can pass through write function
print("completed!!!!!!")    