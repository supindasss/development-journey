"""Task 27 || Movie || 04-03-2026
2. Write a program to count how many movie records are present in move.csv (excluding the header)."""
from csv import DictReader

fr =open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf-8")

data=list(DictReader(fr))

print("Total movie records = ",len(data))

