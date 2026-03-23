"""Task 15 || Pattern || 06-02-2026
15.pascals triangle """
rows = 4
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    val = 1
    for k in range(i + 1):
        print(val, end=" ")
        val = val * (i - k) // (k + 1)    
    print()