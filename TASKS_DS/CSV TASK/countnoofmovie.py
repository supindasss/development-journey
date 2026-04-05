"""Task 27 || Movie || 04-03-2026
8. Read move.csv, calculate how many movies are in each genre (Movie Categories), and write the output into genre_count.txt."""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv",encoding="utf-8")

fw=open("TASKS_DS\CSV TASK\genre_count.txt","w")

data=list(DictReader(fr))

movies_caterogories=[[line.get("Name"),line.get("Movie Categories")] for line in data]  

genere_count={}

for m in movies_caterogories:

    genre=m[1]
    
    if genre in genere_count:
        genere_count[genre]+=1

    else:
        genere_count[genre]=1    
fw.write(str(genere_count))







