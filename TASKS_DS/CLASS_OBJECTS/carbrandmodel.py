"""Task 28 || OOP – Constructor || 10-03-2026
4. Create a class Car with a constructor that initializes brand and model. Print the car details using a method."""

class Car:

    def __init__(self,brand,model):

        self.brand=brand

        self.model=model

    def display(self):

        print(f"model is {self.model} and brand is {self.brand}")  

car_instance=Car("Swift","Maruti Suzuki")    
car_instance.display()        