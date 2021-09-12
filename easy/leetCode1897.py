#1897. Redistribute Characters to Make All Strings Equal
def makeEqual(words):
    charMap = {}
    for word in words:
        for char in word:
            charMap[char] = charMap.get(char,0) + 1
   
    for val in charMap.values():
        if val % len(words) != 0:
            return False

    return True



makeEqual(["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"])