def calculator(*args,**kwargs):

    if kwargs.get("key")=="+":

        return sum(args)
    
    elif kwargs.get("key")=="*":

        p=1

        for num in args:

            p=p*num

        return p     

print(calculator(10,20,30,40,key="+"))

print(calculator(10,20,30,key="*"))

