"""13. Valence Mood Detector
Create a class MoodDetector.
Attributes:
track_name
valence
Create a method to determine if the song mood is:
Happy
Neutral
Sad.  greater 0.6 -happy greater than 0.4=neutral els sad"""

from csv import DictReader
class MoodDetector:

    def __init__(self,track_name,valence):

        self.track_name=track_name

        self.valence=float(valence)

    def displaymood(self):

        if self.valence>=0.6:

            print(f"{self.track_name} _ Happy") 

        elif self.valence>=0.4:

            print(f"{self.track_name} _ Neutral")    

        else:

            print(f"{self.track_name} _ Sad")   

fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

data=list(DictReader(fr))

for row in data:

    t=MoodDetector(row.get("track_name"),row.get("valence"))

    t.displaymood()

        

    