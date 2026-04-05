"""Task 28 || OOP – Constructor || 10-03-2026
1. Create a class Student with a constructor that initializes name and age. Create an object and display the details."""

class Student:
    def __init__(self,name,age):

        self.name=name
        self.age=age

    def display(self):

        print(f"{self.name,self.age}")

student_instance=Student("supindas",22)  

student_instance.display()


        

    

