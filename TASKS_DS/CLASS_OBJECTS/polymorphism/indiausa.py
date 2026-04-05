"""Task 29 || OOP – Polymorphism || 12-03-2026
6. Create two classes India and USA with a method capital(). Print the capital city of each country."""

class India:

    def capital(self):

        print("newdelhi")
class USA(India):

    def capital(self):

        print("Washington")

instance_usa=USA()

instance_india=India()

instance_usa.capital()

instance_india.capital()