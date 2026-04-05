"""Task 27 || Movie || 04-03-2026
9. Read all movies from move.csv and write them into sorted_movies.csv sorted in descending order of rating."""

from csv import DictReader
from csv import DictWriter

fr=open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf-8")
fw=open("TASKS_DS\\CSV TASK\\sorted_movies.csv","w")
data=list(DictReader(fr))
movies=[[line.get("Name"),line.get("Rating")] for line in data]

sor=sorted(movies,key=lambda n:n[1],reverse=1)
for s in sor:
    fw.write(s[0]+"\n")


    



