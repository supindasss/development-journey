
def is_fibonaccinumber(number):
    is_fibo=False
    num1=0
    num2=1
    next=num1+num2
    while(next<=number):
        next=num1+num2
        num1=num2
        num2=next
        if next==number:
            is_fibo=True
            break
    return is_fibo
print(is_fibonaccinumber(10))
print(is_fibonaccinumber(8))