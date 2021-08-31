#1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
def isPrefixOfWord( sentence, searchWord):
    wordArr = sentence.split(" ")
    result  = -1
    for index in range(len(wordArr)):
         word = wordArr[index]
         serchLen = len(searchWord)
         if word[0:serchLen] == searchWord:
             return index + 1
    return result


isPrefixOfWord("hellohello hellohellohello","ell")
