# 804. Unique Morse Code Words
def uniqueMorseRepresentations( words):
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    chars = "abcdefghijklmnopqrstuvwxyz"
    charArr = []
    for char in chars:
        charArr.append(char)
    charMap = dict(zip(charArr,codes))
    codeSet = set()
    for word in words:
        newStr = ""
        for char in word:
            newStr += charMap[char]
        codeSet.add(newStr)
    return len(codeSet)

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))


print(uniqueMorseRepresentations(["a"]))