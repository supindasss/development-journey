"""Task 13 || if, for, while, match || 04-02-2026
9. Write a program using match–case to perform addition, subtraction, multiplication, or division based on user choice."""
num1=int(input("Enter number"))
num2=int(input("Enter second number"))
inp=int(input("enter your choice"))
match inp:
    case 1:print("Addition result",num1+num2)
    case 2:print("Subtracted result ",num1-num2)
    case 3:print("product ",num1*num2)
    case 4:print("division ",num1/num2)
    case _:
        print("Invalid")
