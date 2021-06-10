# 500. Keyboard Row
def findWords( words):
    map, result ,row1, row2, row3 = {}, [], "qwertyuiop", "asdfghjkl", "zxcvbnm"
    for char in row1:
        map[char] = 1
    for char in row2:
        map[char] = 2
    for char in row3:
        map[char] = 3
    for word in words:
        numSet = set()
        for char in word:
            char = char.lower()
            numSet.add(map.get(char))
        if len(numSet) == 1:
            result.append(word)

    return result
 
words = ["adsdf","sfd"]
print(findWords(words))