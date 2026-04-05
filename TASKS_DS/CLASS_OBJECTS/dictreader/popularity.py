"""
3. Popularity Check
Create a class TrackPopularity.
Add a method check_popularity() that prints:
High Popularity if popularity > 80
Medium Popularity if 50–80
Low Popularity if below 50."""
from csv import DictReader

class TrackPopularity:

    def __init__(self):

        self.lst=[]
        self.ls2=[]
        self.ls3=[]

        fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")
        
        self.data=list(DictReader(fr))

        print(len(self.data))

    def display(self):

        self.lst=[s.get("track_name") for s in self.data if int(s.get("popularity"))>80] 

        #print("high popularity",self.lst)

        print("Total",len(self.lst),"high pupularity Records found \n\n\n\n\n\n\n")

        self.ls2=[s.get("track_name") for s in self.data if int(s.get("popularity"))>=50 and int(s.get("popularity"))<=80]

        #print("Medium popularity",self.ls2)

        print("Total",len(self.ls2),"Medium pupularity Records found \n\n\n\n\n\n\n")
        
        self.ls3=[s.get("track_name") for s in self.data if int(s.get("popularity"))<50]

        #print("Low popularity",self.ls3)

        print("Total",len(self.ls3),"Low pupularity Records found \n\n\n\n\n\n\n")
      
instance=TrackPopularity()

instance.display()


