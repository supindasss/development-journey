"""Task 28 || OOP – Constructor || 10-03-2026
9. Create a class Laptop with a constructor that initializes brand and RAM size. Print the laptop specifications."""

class Laptop:

    def __init__(self,brand,ramsize):

        self.brand=brand

        self.ramsize=ramsize

    def display(self):

        print(self.brand,self.ramsize)
Lap=Laptop("HP","16GB")
Lap.display()