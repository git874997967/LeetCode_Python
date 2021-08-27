#1189. Maximum Number of Balloons
def maxNumberOfBalloons(text):
    charMap = {'b':0,'a':0,'l':0,'o':0,'n':0}
    for char in text:
        if char in charMap.keys():
            charMap[charMap] = charMap.get(char) + 1
    count = min(charMap['b'],charMap['a'],charMap['n'])
    doubleCount = min(charMap['l'],charMap['o'])
    return min(count,doubleCount//2)
    
    
