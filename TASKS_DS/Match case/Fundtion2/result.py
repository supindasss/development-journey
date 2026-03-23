"""Task 17 || Function || 10-02-2026
9. Write a function that takes two numbers and an operator (+, -, *, /) as parameters and returns the calculated result."""
def result_operation(n1,n2,operator):
    if operator=="+":
        return n1+n2
    elif operator=="-":
        return n1-n2
    elif operator=="*" or "X" or "x":
        return n1*n2
    elif operator=="/":
        return n1/n2
    else:
        return "invalid"
n1,n2=map(int,input("Enter two numbers ").split())   
operator=input("Enter your operation") 
print(result_operation(n1,n2,operator))