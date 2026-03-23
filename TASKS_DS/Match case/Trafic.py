"""Task 07 || Match case , if etc... || 27-01-2026
12. Write a program to check whether a given character is uppercase or lowercase."""

user=input("Enter the character ")
match user:
    case user if user.islower():
        print("the string is an lowercase")  
    case user if user.isupper():
        print(" the string is upper case ")
          
