"""Task 17 || Function || 10-02-2026
3. Write a function that takes two numbers as parameters and returns their sum."""
def addition(num1,num2):
    return num1+num2
num1=int(input("Enter fisrt numner"))
num2=int(input("Enter second numner"))
print(f"the sum of {num1,num2}are {addition(num1,num2)}")