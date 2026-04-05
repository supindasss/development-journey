"""Task 29 || OOP – Polymorphism || 12-03-2026
5. Create a class Employee with a method work(). Create subclasses Developer and Manager that override the work() method."""

class Employee:

    def work(self):

        print("Employee Working")

class Developer(Employee):

    def work(self):

        print("Developer working")      

class Manager(Employee):

    def work(self):

        print("Manager working")

emp=Employee()

devp=Developer()

manager=Manager()

emp.work()

devp.work()

manager.work()