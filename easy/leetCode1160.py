#1160. Find Words That Can Be Formed by Characters
def countCharacters( words, chars):
    charMap, result = {},   0 
    for char in chars:
        charMap[char] = charMap.get(char,0) + 1 
    
    for word in words:
        wordMap = {}
        length = 0
        for char in word:
            wordMap[char] = wordMap.get(char,0) + 1
        for k,v in wordMap.items():
            if v > charMap.get(k,0):
                break
            else:
                length += 1
        if length == len(wordMap):
            result += len(word)

    return result 
 