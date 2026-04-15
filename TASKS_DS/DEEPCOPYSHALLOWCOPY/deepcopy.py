"""Task 31 || Shallow Copy & Deep Copy || 17-03-2026
4. Write a Python program to perform deep copy using the deepcopy() function from the copy module."""

from copy import deepcopy

original_list=[["blue","red"],["green","purple"],["orange","black"]]

avengers_list=deepcopy(original_list)

avengers_list[0][0]="Blue_nebula"
avengers_list[0][1]="Red_hulk"
avengers_list[1][0]="green_hulk"
avengers_list[1][1]="purple_thanos"
avengers_list[2][0]="orange_thor"
avengers_list[2][1]="black_widow"

print("original list= ",original_list)
print("avengers list= ",avengers_list)




