def count_spam_words(message):

    count=0

    fr=open("CLASSWORKOUTS\\filedictreader\\errorhandling\\spam_words.txt","r")

    word_list=[line.rstrip("\n") for line in fr]

    spam_words_in_message=[w for w in message.split(" ") if w in word_list]

    count=len(spam_words_in_message)

    print(len(spam_words_in_message)/len(message.split(" "))*100)

    return count


print(count_spam_words("you win free  cash"))