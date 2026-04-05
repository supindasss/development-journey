"""Task 27 || Movie || 04-03-2026
3. Write a program to read the header row from move.csv and print all column names."""

from csv import DictReader
 
fr= open("TASKS_DS\\CSV TASK\\move (2).csv", encoding="utf-8")

reader=DictReader(fr)
data=list(reader)

#print(reader.fieldnames)

#accepting a year from the user and displaying it 

year=input("Enter the year")

lst=[line.get("Name") for line in data if line.get("Year of Release")==year]

print(lst)



