"""Task 28 || OOP – Constructor || 10-03-2026
10. Create a class BankAccount with a constructor that initializes account holder name and balance. Display the account details."""

class BankAccount:

    def __init__(self,name,balance):
        
        self.name=name

        self.balance=balance

    def display(self):

        print(f"acc holder name ={self.name} and available balance is {self.balance}")    

bankl=BankAccount("supindas",100000)        

bank2=BankAccount("vipindas",200000)

bankl.display()
bank2.display()