"""Task 30 
1. Create a Track Class
Create a class Track with attributes:
track_name
artist
popularity
Create a method display_info() to print track details."""

from csv import DictReader

class Track:

    def __init__(self):
        
        fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")

        self.spotify=list(DictReader(fr))

        print(len(self.spotify),"records found")

    def display_info(self):

       for s in self.spotify:
           
           self.Track_name=s.get("track_name")

           self.artist=s.get("artists")

           self.popularity=s.get("popularity")

           track_info={"Track_name":self.Track_name,"artists":self.artist,"popularity":self.popularity} 

           print(track_info) 

tracking=Track()
tracking.display_info()

