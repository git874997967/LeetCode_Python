# 266. Palindrome Permutation
def canPermutePalindrome(s):
    if len(s) == 1:
        return True 
    charMap = set()
    for char in s:
        if char not in charMap:
            charMap.add(char)
        else:
            charMap.remove(char)
    return len(charMap) > 1

print(canPermutePalindrome("code"))

print(canPermutePalindrome("aab"))

print(canPermutePalindrome("aa"))

print(canPermutePalindrome("carerac"))