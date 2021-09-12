#1935. Maximum Number of Words You Can Type
def canBeTypedWords(text, brokenLetters):
    badWord = 0 
    for word in text.split(' '):
        for char in word:
             
            if char in brokenLetters:
                badWord += 1
            break
        continue
    return len(text.split(' ') ) - badWord

canBeTypedWords("leet code","lt")