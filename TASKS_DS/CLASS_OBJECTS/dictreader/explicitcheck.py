"""8. Explicit Content Check
Create a class TrackSafety.
Attributes:
track_name
explicit
Create a method check_content() to display whether the track is Explicit or Clean."""

from csv import DictReader

class TrackSafety:

    def __init__(self,track_name,explicit):

        self.track_name=track_name

        self.explicit=explicit

    def check_content(self):

        if self.explicit==True:

            print(f"{self.track_name} is explicit")

        else:

            print(f"{self.track_name} is clean")

fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

data=list(DictReader(fr))

for row in data:
    t=TrackSafety(row.get("track_name"),row.get("explicit"))
    t.check_content()
