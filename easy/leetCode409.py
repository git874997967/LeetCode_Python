# 409. Longest Palindrome
def longestPalindrome( s):
    if len(s) == 1:
        return 1
    result,charDict,oddCount = 0 , {},True 
    for char in s:
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] += 1
    for count in charDict.values():
        if count % 2 == 0:
            result += count
        else:
            result += count - 1
            oddCount = False
    return result  if oddCount else result + 1  