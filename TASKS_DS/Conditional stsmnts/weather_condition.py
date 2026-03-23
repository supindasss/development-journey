"""TASK-04 || if else,if elif else 
8.Write a Python program to display weather conditions based on temperature:

Above 30 → Hot
20 to 30 → Warm
Below 20 → Cold

"""
weather=int(input("Enter current weather in %"))
if weather>30:
    print("Hot")
elif weather>20 and weather<=30:
    print("Warm")
elif weather<=20:
    print("cold")
else:
    print("invalid entry")
