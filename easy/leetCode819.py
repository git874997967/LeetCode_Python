# 819. Most Common Word\
import re
def mostCommonWord( paragraph, banned):
    wordMap = {}
    words = re.sub(r'[^\w]',' ',paragraph)
    wordArr = words.split(" ")
    maxCount = 0
    newBanned = [w.lower() for w in banned]
    print(newBanned)
    for word in wordArr:
        newWord = word.lower()
        if not word.isalpha():
            continue
        if newWord not in newBanned:
            wordMap[newWord] = wordMap.get(newWord,0 ) + 1
    print(wordMap)
    for k,v in wordMap.items():
        if v > maxCount:
            
            result = k
            maxCount = v
    print(result)
    return result

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
 

mostCommonWord(paragraph, banned)