"""14. Track Summary Class
Create a class TrackSummary.
Attributes:
track_name
artist
genre
popularity
Create a method summary() to print all information."""

from csv import DictReader

class TrackSummary:

    def __init__(self,track_name,artist,genre,popularity):

        self.track_name=track_name

        self.artist=artist

        self.genre=genre

        self.popularity=popularity

    def summary(self):

        self.lst=[{"track_name":self.track_name},{"artist":self.artist},{"genre":self.genre},{"popularity":self.popularity}] 
        print(self.lst)   
fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

data=list(DictReader(fr))

for row in data:

    D=TrackSummary(row.get("track_name"),row.get("artists"),row.get("track_genre"),row.get("popularity"))
    D.summary()