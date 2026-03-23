def add(*args):

    return sum(args)

def largest_of_numbers(*args):

    return max(args)

def count_of_evens(*args):

    evens={num for num in args if num%2==0}

    return len(evens)

def count_of_odds(*args):

    odds={num for num in args if num%2!=0}

    return len(odds)

def product_of_numbers(*args):

    p=1

    for num in args:

        p=p*num

    return p    


print(add(10,20,30,40,50,60))

print(add(10,20,30,40))

print(f"largest of numbers={largest_of_numbers(10,80,90,25,35,40)}")

print("Totakl even numbers = ",count_of_evens(10,11,12,13,14,15,16,17,18,19,20))

print("odd_numbers = ",count_of_odds(10,11,12,13,14,15,16,17,18,19,20))

print("product of numbers = ",product_of_numbers(10,20,30,40,50))

print("product of this numbers = ",product_of_numbers(5,6,7,9))






