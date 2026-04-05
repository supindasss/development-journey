"""Task 28 || OOP – Constructor || 10-03-2026
5. Create a class Circle with a constructor that takes radius. Write a method to calculate the area of the circle."""

class Circle:

    def __init__(self,radious):
        
        self.radious=radious

    def display(self):

        print("the area of circle is ",3.14*(self.radious**2))  

circle_instance=Circle(6)

circle_instance.display()