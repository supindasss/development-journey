class Marvell():

    def __init__(self,marvel_cinimatic):

        self.marvel_cinimatic=marvel_cinimatic

    def display(self):

        print(self.marvel_cinimatic)

class IronMan(Marvell):

    def __init__(self, marvel_cinimatic,movie_name,character):

        super().__init__(marvel_cinimatic)   

        self.movie_name=movie_name

        self.character=character 

    def display(self):

        super().display()

        print(self.movie_name,self.character)

iron_instance=IronMan("MCU","Iron man","Tony stark")     

iron_instance.display()


