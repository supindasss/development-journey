"""Task 29 || OOP – Polymorphism || 12-03-2026
7. Create a class Shape with a method draw(). Create subclasses Square and Triangle that override the draw() method."""

class Shape:

    def draw(self):

        print("Drwaing the shapes")

class Squre(Shape):

    def draw(self):

        print("Drawing squrebs")

class Triangle(Shape):

    def draw(self):

        print("drawing Triangle")

shape=Shape()
squre=Squre()
triangle=Triangle()

shape.draw()

squre.draw()

triangle.draw()


