"""TASK 22 || Python Collections || 24-02-2026
13. Remove a specific key from a dictionary and print the updated dictionary."""
dictionery={"name":"supindas","age":22,"course":"python datascience machine learning"}
print(f"dictionery before removing a key {dictionery}")
removed=dictionery.pop("name","key not found")
print(dictionery)
print("the removed key is ",removed)