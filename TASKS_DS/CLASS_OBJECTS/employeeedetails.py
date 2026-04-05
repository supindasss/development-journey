"""Task 28 || OOP – Constructor || 10-03-2026
3. Create a class Employee with a constructor that initializes employee name and salary. Display the employee details."""

class Employee:

    def __init__(self,name,salary):

        self.name=name

        self.salary=salary

    def display(self):   

        print("the details of employees are ",self.name,self.salary) 

employee_instance=Employee("supindas v",35000)

employee_instance.display()
