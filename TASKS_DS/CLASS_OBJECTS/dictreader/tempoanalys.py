"""7. Tempo Analysis
Create a class TempoAnalyzer.
Attributes:
track_name
tempo
Create a method to classify:
Slow
Medium
Fast."""

from csv import DictReader

class TempoAnalysis:

    def __init__(self,track_name,tempo):

        self.track_name=track_name

        self.tempo=tempo

    def classify(self):

        if float(self.tempo)<80:

            print(f"{self.track_name} --slow") 

        elif 80<=float(self.tempo)<=120:

            print(f"{self.track_name} --medium")

        else:

            print(f"{self.track_name} --fast")  
fr=open("TASKS_DS\\CLASS_OBJECTS\\dictreader\\spotify-tracks-dataset.csv",encoding="utf-8")
data=list(DictReader(fr))
for row in data:
    t=TempoAnalysis(row.get("track_name"),row.get("tempo"))

    t.classify()

        