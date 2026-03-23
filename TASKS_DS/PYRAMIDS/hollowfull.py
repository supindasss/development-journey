"""Task 15 || Pattern || 06-02-2026
11.Hollowfullpyramid """
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        if k==1 or k==i or i==5:
            print("*",end=" ")
        else:
            print("  ",end="")        
    print()        