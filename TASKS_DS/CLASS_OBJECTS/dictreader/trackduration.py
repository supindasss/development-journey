"""Task 30 
2. Track Duration
Create a class TrackDuration with attributes:
track_name
duration_ms
Create a method to convert duration from milliseconds to minutes."""

from csv import DictReader

class TrackDuration:

    def __init__(self):

        fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

        self.data=list(DictReader(fr))

        print(f"{len(self.data)} founded")

    def millisecondTominutes(self):

        for m in self.data:

            self.Trackname=m.get("track_name")

            self.duration_in_ms=int(m.get("duration_ms"))

            self.du_in_minutes=self.duration_in_ms/60000

            list={"Name":self.Trackname,"minutes":self.du_in_minutes}

            print(list)

D_instance=TrackDuration()

D_instance.millisecondTominutes()


        

