"""Task 29 || OOP – Polymorphism || 12-03-2026
1. Create two classes Dog and Cat. Both classes should have a method sound(). Print different sounds for each animal."""

class Dog:
    def sound():
        print("this is dog sound")

class Cat(Dog):
    def sound():
        print("this is cat sound")   

cat=Cat.sound()
dog=Dog.sound()