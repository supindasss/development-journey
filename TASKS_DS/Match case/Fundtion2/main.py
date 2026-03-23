"""Task 17 || Function || 10-02-2026
10. Write a function that takes a number as a parameter and returns True if it is a prime number, otherwise returns False."""
def test_primr(number):
    if number==1:
        return False
    elif number==2:
        return True
    else:
        for i in range(2,number):
            if number%i==0:
                return False
        return True
number=int(input("Enter number "))
print(test_primr(number))
