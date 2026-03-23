word1=input("enter fisrt word")
word2=input("eneter second word")
if len(word1)>len(word2):
    print(f"{word1[len(word1):]}")
elif len(word2)>len(word1):
    print(f"{word2[len(word1):]}")
else:
    print("no")
