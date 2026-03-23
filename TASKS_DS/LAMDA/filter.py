"""Task 25 || Lambda Function || 02-03-2026
5. Use a lambda function with filter() to get all even numbers from a list."""
lst=[10,9,8,7,6,5,4,3,2,1]
filterr=list(filter(lambda num: num%2==0,lst))
print(filterr)
