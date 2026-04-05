"""Task 28 || OOP – Constructor || 10-03-2026
7. Create a class Product with a constructor that initializes product name and price. Print the product details."""

class Product:

    def __init__(self,p_name,p_price):

        self.p_name=p_name

        self.p_price=p_price

    def display(self):

        print(self.p_name,self.p_price)    

product_instance=Product("Cutie the beauty soap",20)   

product_instance.display()

        