def analyze_numbers(*args,**kwargs):

    if kwargs.get("action")=="max":

        return max(args)
    
    elif kwargs.get("action")=="min":

        return min(args)
    
    elif kwargs.get("action")=="count":

        return len(args)
    
print(analyze_numbers(10,11,12,13,14,15,action="max"))

print(analyze_numbers(10,11,12,13,14,15,action="min"))

print(analyze_numbers(10,11,12,13,14,15,action="count"))

