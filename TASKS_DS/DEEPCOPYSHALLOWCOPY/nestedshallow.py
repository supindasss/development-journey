"""Task 31 || Shallow Copy & Deep Copy || 17-03-2026
3. Create a list containing nested lists. Perform a shallow copy and modify the inner list. Print both lists and observe the result."""

original_list=[["blue","red"],["green","purple"],["orange","black"]]

copy_list=original_list[0].copy()

copy_list[0]="blue_nebula"
copy_list[1]="red_hulk"

print("original_list= ",original_list)

print("copy_list= ",copy_list)

