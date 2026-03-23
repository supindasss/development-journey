def mark_calculator(*args,**kwargs):

    if kwargs.get("option")=="average":

        avg=sum(args)/len(args)

        return avg 

    elif kwargs.get("option")=="total":

        return sum(args)
   

    elif kwargs.get("option")=="highest":

        return max(args)

print(mark_calculator(35,45,45,47,45,option="average"))

print(mark_calculator(35,45,45,47,45,option="total"))

print(mark_calculator(35,45,45,47,45,option="highest"))