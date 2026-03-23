word=input("Enter the string")
word_length=len(word)-1
result=""
for i in range(word_length,-1,-1):
    result=result+word[i]
if result==word:
    print("its palindrom")
else:
    print("not palindrom")        