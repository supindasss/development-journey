"""12. Instrumental Track
Create a class InstrumentalTrack.
Attributes:
track_name
instrumentalness
Create a method to check whether the song contains vocals or only instruments."""

from csv import DictReader

class InstrumentalTrack:

    def __init__(self,track_name,instrumentalness):

        self.track_name=track_name

        self.instrumentalness=float(instrumentalness)

    def check(self):

        if self.instrumentalness>=0.5:
            print(f"{self.track_name} - instrumental(NO VOCALS)")

        else:
            print(f"{self.track_name} - contain vocals")

fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

data=list(DictReader(fr))

for row in data:

    k=InstrumentalTrack(row.get("track_name"),row.get("instrumentalness"))

    k.check()
        