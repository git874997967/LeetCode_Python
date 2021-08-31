#1370. Increasing Decreasing String
def sortString(s):
    charMap ,result = {},[]
    for char in s:
        charMap[char] = charMap.get(char,0) + 1

    while len(charMap) != 0:
        incOrder = sorted(charMap)
        result += incOrder
        for k in incOrder:
            charMap[k] = charMap.get(k) - 1
            if charMap[k] == 0:
                del charMap[k]
        incOrder = sorted(charMap)
        result += incOrder[::-1]
        for k in incOrder:
            charMap[k] = charMap.get(k,0) - 1
            if charMap[k] <= 0:
                del charMap[k]
    print(''.join(result))
    return ''.join(result)

# sortString("aaaabbbbcccc")
# sortString("rat")
# sortString("leetcode")
# sortString("spo")
sortString("gtqxozxzrssrzxzoxqtg")
