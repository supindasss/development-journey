"""Task 15 || Pattern || 06-02-2026
6.inverted full pyramid"""
for i in range(6,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(" * ",end="")
    print()        