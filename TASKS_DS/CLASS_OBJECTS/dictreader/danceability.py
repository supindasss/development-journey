"""6. Danceability Class
Create a class DanceTrack.
Attributes:
track_name
danceability
Create a method to check if the song is good for dancing (danceability > 0.7)."""

from csv import DictReader

class DanceTrack:

    def __init__(self):

        fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.track_name:str
        self.danceability:float
        self.data=list(DictReader(fr))

    def dancing(self):
        self.dict={k.get("track_name"):k.get("danceability") for k in self.data if float(k.get("danceability"))>0.7}
        print(len(self.dict),"records found")
        print(self.dict,"these are the songs good for dancing")
        
instance=DanceTrack()

instance.dancing()