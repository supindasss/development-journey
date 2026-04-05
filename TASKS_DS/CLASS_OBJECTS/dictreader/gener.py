"""
4. Genre Class
Create a class Genre.
Attributes:
track_name
track_genre
Create a method show_genre() to display genre details."""

from csv import DictReader

class Genre:

    def __init__(self):
        fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.track_name=str
        self.track_genre=str
        self.data=list(DictReader(fr))   

    def show_genre(self):

        dictionery=[[n.get("track_name"),n.get("track_genre")] for n in self.data]      
            
        print(dictionery)           

genre_instance=Genre()

genre_instance.show_genre()



                








        
