"""9. Artist Information
Create a class Artist.
Attributes:
artist_name
track_name
Create a method to print all details."""
from csv import DictReader

class Artist:

    def __init__(self,track_name,artist_name):

        self.artist_name=artist_name

        self.track_name=track_name

    def display(self):

        print(f"{self.track_name} by {self.artist_name}") 

fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")   

data=list(DictReader(fr))

for row in data:

    k=Artist(row.get("track_name"),row.get("artists"))

    k.display()