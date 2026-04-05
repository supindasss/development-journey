"""Task 29 || OOP – Polymorphism || 12-03-2026
4. Create two classes Car and Bike. Both classes should have a method start() that prints different messages."""

class Car:

    def start(self):

        print("Car strating")

class Bike(Car):

    def start(self):

        print("bike starting")        
car=Car()
bike=Bike()

car.start()
bike.start()