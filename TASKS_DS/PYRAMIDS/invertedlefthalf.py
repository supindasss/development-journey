"""Task 15 || Pattern || 06-02-2026
5.inverted left  half pyramid"""
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")    
    print()    