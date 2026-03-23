"""Task 25 || Lambda Function || 02-03-2026
8. Write a Python program to count the number of words in a file."""
word=open("TASKS_DS\\Fileoperations\\word.txt","r")
lst=[]
for drinks in word:
    cleaned=drinks.rstrip("\n")
    lst.append(cleaned)
    word_count={o:lst.count(o) for o in lst}
print(word_count)    

