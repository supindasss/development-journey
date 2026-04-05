"""Task 28 || OOP – Constructor || 10-03-2026
2. Create a class Rectangle with a constructor that takes length and width. Write a method to calculate the area of the rectangle."""
class Rectangle:
    def __init__(self,length,width):

        self.length=length

        self.width=width

    def display(self):

        print("the area of rectangle is = ",self.length*self.width)    

rectange_instance=Rectangle(10,12)
rectange_instance.display()        
