from csv import DictReader

fr =open("TASKS_DS\\Fileoperations\\movies.csv")

data=list(DictReader(fr))

print(data)