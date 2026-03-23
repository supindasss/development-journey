"""CONDITIONAL LOGIC PRACTICE QUESTIONS TASK -08
8. Restaurant Order System
  """
food="Beef_fry"
user=int(input("Enter the table number "))
if user in range(1,11):
    print("Your table is ready")
    fin=input("Enter your meal")
    if fin==food:
        print("This food is available , have the seat ")
    else:
        print(" OOps Next time!!...the specific food is not available righnt now  ")
else:
    print("The Table is not ready....")            
