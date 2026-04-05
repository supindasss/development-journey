"""Task 27 || Movie || 04-03-2026
6. Accept a genre from the user (e.g., Action, Drama, Romance) and print all matching movies from move.csv."""

from csv import DictReader

fr=open("TASKS_DS\\CSV TASK\\move (2).csv")

data=list(DictReader(fr))

gener=input("enter your gner ")

matching_movies=[movie.get("Name") for movie in data if movie.get("Movie Categories")==gener]

print(f"The movie with {gener} is {matching_movies}")

