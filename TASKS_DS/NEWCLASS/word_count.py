text="python programming programming programming is simple"
words=text.split(' ')
wordcount={w:words.count(w) for w in words }
print(wordcount)