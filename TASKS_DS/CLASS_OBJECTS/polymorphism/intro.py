"""Task 29 || OOP – Polymorphism || 12-03-2026
10. Create a class Vehicle with a method move(). Create subclasses Car and Airplane that override the move() method."""

class Vehicle:

    def move(self):

        print("Vehicles moving")

class Car(Vehicle):

    def move(self):

        print("Car moving")

class Airplane(Vehicle):

    def move(self):

        print("Airplane moving")         

airplane=Airplane()

car=Car()

airplane.move()

car.move()
