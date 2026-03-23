"""TASK-04 || if else,if elif else 
5.Write a Python program to check whether a student passed or failed (pass mark: 40).
6️ Write a Python program to display the grade of a student using the following rules:
Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Fail
"""
mark=int(input("Enter your obtained mark"))
if mark>=90:
    print("A grade")
elif mark>=75:
    print("B grade")
elif mark>=50:
    print("C grade")
else:
    print("You are failed")  
