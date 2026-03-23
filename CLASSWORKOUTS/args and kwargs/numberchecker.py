def number_cheker(*args,**kwargs):

    if kwargs.get("type")=="odd":

        odds=[num for num in args if num%2!=0]

        return len(odds)
    
    elif kwargs.get("type")=="even":

        evens=[num for num in args if num%2==0]

        return len(evens)
    
    elif kwargs.get("type")=="positive":

        postive=[num for num in args if num>0]

        return len(postive)
    
    elif kwargs.get("type")=="negative":

        negative=[num for num in args if num<0]
  
        return len(negative)
    
print(number_cheker(0,11,12,13,14,15,type="odd")) 

print(number_cheker(0,11,12,13,14,15,type="even")) 

print(number_cheker(0,11,12,13,14,15,type="positive"))

print(number_cheker(0,11,12,-13,14,-15,type="negative")) 

