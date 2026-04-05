"""Task 27 || Movie || 04-03-2026
7. Create a new CSV file named top_rated.csv and write all movies from move.csv with a rating greater than 8.0."""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf-8")
fw=open("TASKS_DS\\CSV TASK\\top_rated.csv","w")

data=list(DictReader(fr))

movies_top_rate=[line.get("Name") for line in data if float(line.get("Rating"))>8.0]

fw.write(str(movies_top_rate))

