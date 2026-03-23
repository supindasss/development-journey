num=int(input("Enter the number "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
print(sum)
if sum==num:
    print("perfect number ")
else:
    print("Not perfect number ")    