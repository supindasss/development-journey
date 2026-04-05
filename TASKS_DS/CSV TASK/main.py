"""Task 27 || Movie || 04-03-2026
10. Read move.csv and print all rows where any field i"""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf=8")

data=list(DictReader(fr))

for line in data:
    print(line)

