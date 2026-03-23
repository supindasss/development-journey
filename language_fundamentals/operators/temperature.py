user=True
while user :
    Celcius=float(input("Enter the temperature in degree celcious"))
    farenheit=(Celcius*9//5)+32
    print("the temperature in farenheat is ",farenheit)
    user=input("do  you wish to continue??")
    if user=="NO" or user=="no" :
        print("thank you visit again !!!!!")
        user=False
