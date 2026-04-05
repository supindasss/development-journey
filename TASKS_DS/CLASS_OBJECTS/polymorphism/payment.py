"""Task 29 || OOP – Polymorphism || 12-03-2026
8. Create a class Payment with a method pay(). Create subclasses CreditCard and UPI that override the pay() method."""

class Payment:

    def pay(self):

        print("paymenting process")

class CreditCard(Payment):

    def pay(self):

        print("payment by credit card")

class UPI(Payment):

    def pay(self):

        print("payment bu UPI")

cc=CreditCard()
Up=UPI()

cc.pay()

Up.pay()