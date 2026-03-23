"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
10. Given a set of numbers, remove all elements greater than 50."""
sett={10,65,20,50,5,75,30,45}
filtered={num for num in sett if num>50}
print(filtered,"is the filterd list ")