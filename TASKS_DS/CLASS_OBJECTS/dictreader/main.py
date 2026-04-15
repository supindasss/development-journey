"""
15. Playlist Class
Create a class Playlist.
Store multiple Track objects in a list.
Create methods to:
Add tracks
Display all tracks
Count total tracks."""
from csv import DictReader

class Playlist:

    def __init__(self):

        self.track=[]

    def addtracks(self,track_name,artist,genre,popularity):
        dictionary={
            "track_name":track_name,
            "artist":artist,
            "genre":genre,
            "popularity":popularity
        }

        self.track.append(dictionary)

    def display(self):
        if not self.track:
            print("the list is empty") 

        else:
            for track in self.track:
                print(track)

    def counttracks(self):

        print("Total count of tracks",len(self.track)) 

play=Playlist()       

play.addtracks("What A Beautiful Name","Hillsong Worship","world-music","66")
play.addtracks("Who You Say I Am","Hillsong Worship;Brooke","Ligertwood","78")

play.display()

play.counttracks()        