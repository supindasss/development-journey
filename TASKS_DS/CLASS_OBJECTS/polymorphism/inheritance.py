"""Task 29 || OOP – Polymorphism || 12-03-2026
3. Create a class Bird with a method fly(). Create subclasses Sparrow and Ostrich that override the fly() method with different behaviors."""

class Bird:

    def fly(self):

        print("Bird flys")

class Sparrow(Bird):

    def fly(self):

        print("sparrow flys")  

class Ostrich(Bird):

    def fly(self):

        print("ostrich cant fly")             

Ostrich_instance=Ostrich()
sparrow_instance=Sparrow()
bird_instance=Bird()

Ostrich_instance.fly()

sparrow_instance.fly()

bird_instance.fly()