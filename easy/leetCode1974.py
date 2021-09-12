#1974. Minimum Time to Type Word Using Special Typewriter
def minTimeToType(word):
    result = 0
    prev = 'a'
    for i in range(len(word)):
        curIndex = ord(word[i]) -97
        preIndex = ord(prev) - 97
        if curIndex >= preIndex:
            dis = min(curIndex - preIndex, preIndex - curIndex + 26)
        else:
            dis = min(preIndex - curIndex, curIndex - preIndex + 26)
        result += dis 
        result += 1
        prev = word[i]
    print(result)
    return result

minTimeToType("abc")
minTimeToType("bza")
minTimeToType("zjpc")
 
minTimeToType("abcdevdewvssxdaacssr")
