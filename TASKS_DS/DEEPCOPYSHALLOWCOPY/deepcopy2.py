"""Task 31 || Shallow Copy & Deep Copy || 17-03-2026
5. Create a nested list and perform deep copy. Modify the inner list and show that the original list remains unchanged."""

from copy import deepcopy

meal=[{"break_fast":"idly","lunch":"biriyani","dinner":"mandhi"},
      {"break_fast":"dosa","lunch":"oonu","dinner":"biriyani"},
      {"break_fast":"pazamkanji","lunch":"porotta","dinner":"chappathi"}]

my_meal=deepcopy(meal)

my_meal[0]["break_fast"]="vellachor"
my_meal[0]["lunch"]="sadhya"
my_meal[0]["dinner"]="choor"

print("original_list =",meal,"THIS LIST REMAILS UNCHANGED")

print("extracted list =",my_meal)