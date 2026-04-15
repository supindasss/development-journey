"""
11. Acoustic Song Check
Create a class AcousticTrack.
Attributes:
track_name
acousticness
Create a method to check if the track is Acoustic or Non-Acoustic."""

from csv import DictReader

class AcousticTrack:

    def __init__(self,track_name,acousticness):

        self.track_name=track_name

        self.acousticness=float(acousticness)

    def display(self):

        if self.acousticness>=0.5:

            print(f"{self.track_name} - acoustic")

        else:

            print(f"{self.track_name} - non acoustic")   

fr=open("TASKS_DS\CLASS_OBJECTS\dictreader\spotify-tracks-dataset.csv",encoding="utf-8")  

data=list(DictReader(fr))

for row in data:

    a=AcousticTrack(row.get("track_name"),row.get("acousticness"))

    a.display()

