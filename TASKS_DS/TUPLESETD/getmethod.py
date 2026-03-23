"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
16. Write a program to safely access a key from a dictionary without causing an error if the key does not exist."""
dictionery={"name":"supindas","designation":"Asst accountant"}
value=dictionery.get('salary','this item is does not exist in the dictionery')
print(value)