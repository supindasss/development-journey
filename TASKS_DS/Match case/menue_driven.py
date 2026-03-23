"""Task 07 || Match case , if etc... || 27-01-2026
3. Create a menu-driven program using match–case for basic arithmetic operations:
* 1 → Addition
* 2 → Subtraction
* 3 → Multiplication
* 4 → Division"""
n1=int(input("Enter 1st number "))
n2=int(input("Second number "))
user=input("Which operation u like to perform, + - X /")
match user:
    case "+":
        print("sum=",n1+n2)
    case "-":
        print("Subtraction",n1-n2)
    case "x":
        print("product=",n1*n2)
    case "/":
        print("Division",n1/n2)
    case _:
        print("invalid entry ")
                       
