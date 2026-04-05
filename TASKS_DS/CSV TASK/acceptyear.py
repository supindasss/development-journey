"""Task 27 || Movie || 04-03-2026
4. Accept a year from the user and display all movie titles released in that year from move.csv."""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf-8")

data=list(DictReader(fr))

year=input("Enter Year")

movies=[line.get("Name") for line in data if line.get("Year of Release")==year]

print(f"movies relaesed in the year {year}= {movies}")