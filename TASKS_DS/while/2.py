"""TASK 10 || While loop || 30-01-2026
10. Write a program to find the sum of digits of a given number using a while loop."""
user=int(input("Enter The number"))
sum=0
while(0<user):
   last=user%10
   sum=sum+last
   user=user//10
print(f"{sum}")   