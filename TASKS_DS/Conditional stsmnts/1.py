"""Task 07 || Match case , if etc... || 27-01-2026
20. Write a program to determine exam result category.
* Marks ≥ 90 → Distinction
* Marks ≥ 60 → First class
* Marks ≥ 40 → Pass
* Below 40 → Fail """
user=int(input("enter the Mark "))
if user>=90:
    print("Distinction")
elif user>=60:
    print("First class")
elif user>=40:
    print("Pass")   
else:
    print("fail")

   
       

