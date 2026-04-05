"""Task 28 || OOP – Constructor || 10-03-2026
6. Create a class Person with a constructor that initializes name and city. Display the information."""

class Person:

    def __init__(self,name,city):

        self.name=name

        self.city=city

    def display(self):

        print(self.name,"from",self.city)    

person=Person("supindas v","pattambi")    
person.display()    
        