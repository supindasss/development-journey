"""TASK 22 || Python Collections || 24-02-2026
14. Write a program to get all items (key-value pairs) from a dictionary."""
dictionery={"name":"supindas","age":22,"course":"python datascience machine learning"}
all=dictionery.items()
print(all)
for k,v in dictionery.items():
    print(f"key:{k} value:{v}")