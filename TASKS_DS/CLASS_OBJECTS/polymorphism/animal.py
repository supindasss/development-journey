"""Task 29 || OOP – Polymorphism || 12-03-2026
9. Create a class Animal with a method eat(). Create subclasses Lion and Cow that override the eat() method.
"""

class Animal:

    def eat(self):

        print("Animal eating")

class Lion(Animal):

    def eat(self):

        print("lion eating")

class Cow(Animal):

    def eat(self):
        print("Cow eating")

lion=Lion()
cow=Cow()

lion.eat()

cow.eat()