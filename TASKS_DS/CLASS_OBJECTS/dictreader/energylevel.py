"""
5. Energy Level
Create a class EnergyLevel.
Attributes:
track_name
energy
Create a method that prints:
High Energy Song
Medium Energy Song
Low Energy Song."""

from csv import DictReader

class EnergyLevel:
    def __init__(self):

        fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data=list(DictReader(fr))
        print(len(self.data),"records founded")

    def display(self):  
        lst=[[e.get("track_name"),e.get("energy")] for e in self.data ]
        high_energ_song=max(lst,key=lambda n:n[1])

        low_energ_song=min(lst,key=lambda l:l[1])

        print("the maximum energy level= ",high_energ_song)

        print("the minimum energy level = ",low_energ_song)
        
energy_instance=EnergyLevel()
energy_instance.display()

