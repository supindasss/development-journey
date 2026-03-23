"""Task 17 || Function || 10-02-2026
8. Write a function that takes a string as a parameter and returns the number of vowels in it."""
word=input("Enter the string ")
def vowels_find(word):
    sum=0
    vowels="aeiou"
    for char in word:
        if char in vowels:
            sum=sum+1
    print(sum)
vowels_find(word)       
     
