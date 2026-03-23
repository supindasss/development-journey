"""TASK 22 || Python Collections || 24-02-2026
8. Given a tuple of numbers, count how many times a specific number appears."""
tupl=(10,20,20,20,20,20,20,5,0,5,5,6,7,0,70,70,70,80,92,6,4)
serch=20
def tuple_element_count(serch):
    count=0
    for numb in tupl:
        if numb==serch:
            count=count+1
    print(f"the numnber {serch} is presented in the list with {count} times")  
tuple_element_count(serch)        
