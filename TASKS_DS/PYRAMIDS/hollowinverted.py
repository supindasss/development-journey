"""Task 15 || Pattern || 06-02-2026
12.Hollow Inverted fullpyramid """
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for k in range(1,i+1):
        if k==1 or k==i or i==5:
            print("*",end=" ")
        else:
            print("  ",end="")        
    print()    