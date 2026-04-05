"""Task 29 || OOP – Polymorphism || 12-03-2026
2. Create two classes Rectangle and Circle. Both classes should have a method area(). Calculate the area for each shape."""

class Rectangle:

    def __init__(self,width,length):

        self.width=width

        self.length=length

    def area(self):

        print("Area of this rectangle is = ",self.width*self.length)   

class Circle(Rectangle):

    def __init__(self,radius):

        self.radius=radius     

    def area(self):

        print("area of the circle is ",3.14*(self.radius**2))      

rectangle_instance=Rectangle(5,2)    
circle_instance=Circle(6)     

rectangle_instance.area()    

circle_instance.area()