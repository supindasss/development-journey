word=input("eneter text")
word_length=len(word)-1
result=""
for i in range(word_length,-1,-1):
    result=result+word[i]
print(result)    
