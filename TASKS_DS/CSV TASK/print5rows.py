"""Task 27 || Movie || 04-03-2026
Use the move.csv file and do all questions
1. Write a Python program to read the file move.csv and print the first 5 rows."""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf-8")

data=list(DictReader(fr))

print(data[0:5])    