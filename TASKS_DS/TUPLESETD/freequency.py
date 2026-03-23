"""Task 21 || Tuple, Set & Dictionary || 23-02-2026
12. Write a program to count the frequency of each character in a string using a dictionary."""
text="hello world"
freequency={ch:text.count(ch) for ch in text if text.count(ch)}
print(freequency)
"""for char in text:
    if char in freequency:
        freequency[char]+=1
    else:
        freequency[char]=1 
print("charcter freequency")
print(freequency) """       