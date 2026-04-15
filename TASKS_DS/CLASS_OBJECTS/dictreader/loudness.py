"""10. Loudness Class
Create a class LoudnessCheck.
Attributes:
track_name
loudness
Create a method to classify:
Loud
Medium
Soft."""

from csv import DictReader

class LoudnessCheck:

    def __init__(self,track_name,loudness):

        self.trcak_name=track_name

        self.loudness=float(loudness)

    def display(self):

        if self.loudness>=-8:

            print(f"{self.trcak_name}  is loud")

        elif self.loudness>=-15:

            print(f"{self.trcak_name} is medium")   

        else:

            print(f"{self.trcak_name} is low ")       
fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

data=list(DictReader(fr))

for row in data:

    t=LoudnessCheck(row.get("track_name"),row.get("loudness"))
    t.display()