"""Task 27 || Movie || 04-03-2026
5. Read move.csv and print the movie with the highest rating."""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv")

data=list(DictReader(fr))

movies_Rating=[[line.get("Name"),line.get("Rating")] for line in data]

maximum=max(movies_Rating,key=lambda n:n[1])

print(f"the mnovie with highest rating is = {maximum}")







