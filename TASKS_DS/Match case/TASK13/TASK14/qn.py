"""Task 14 || Nested loop || 05-02-20265.
Write a program using nested loops to print the following:"""

"""1
   1
   1"""

#(Outer loop runs 3 times, inner loop runs once)
for i in range(1,4):
    for j in range(1,2):
        print(j,end="")
    print()    