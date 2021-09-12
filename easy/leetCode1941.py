#1941. Check if All Characters Have Equal Number of Occurrences
def areOccurrencesEqual(s):
    charMap = {}
    for char in s:
        charMap[char] = charMap.get(char,0) + 1
    val = charMap.get(s[0])
    for v in charMap.values():
        if v != val:
            return False

    return True