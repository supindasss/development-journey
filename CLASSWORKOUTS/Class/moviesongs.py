class Movie:
    def __init__(self,title,language):

        self.title=title

        self.language=language

    def display(self):

        print(self.title,self.language)

class Songs(Movie):

    def __init__(self,title,language,name,track_number,singer):

        super().__init__(title,language)   

        self.name=name

        self.track_number=track_number

        self.singer=singer

    def display(self):

        super().display()   

        print(self.name,self.track_number,self.singer)

song_instance=Songs("bahubali","telugu","kallumthooki",1,"vijayalakshmi")

song_instance.display()