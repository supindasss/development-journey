"""Task 25 || Lambda Function || 02-03-2026
10. Write a Python program to copy the contents of one file to another file."""
orginal_file=open("TASKS_DS\\Fileoperations\\appending.txt","r")
copy_file=open("TASKS_DS\Fileoperations\createandwritefile.txt","a")
lst=[name for name in orginal_file]
for character in lst:
    copy_file.write(character+"\n")
print("the exicution is completed !!! the contects of file appending.txt is appended to the file createandwritefile.txt ")

