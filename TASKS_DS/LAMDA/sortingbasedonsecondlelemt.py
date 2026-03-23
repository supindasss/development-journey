"""Task 25 || Lambda Function || 02-03-2026
4. Write a Python program to sort a list of tuples based on the second element using a lambda function."""
fruits=[("apple",289),("orange",150),("pinapple",230),("watermelon",20),("grapes",80)]
fruits.sort(key=lambda kp:kp[1])
print(fruits)