# 387. First Unique Character in a String
def firstUniqChar(s):
    result = float('inf')
    dict = {}
    for index in range(len(s)):
        if s[index] in dict:
            dict[s[index]] = -1
        else:
            dict[s[index]] = index 
    for index in dict.values():
        if index >= 0:
            result = min(index, result)
    return -1 if result == float('inf') else result 

print(firstUniqChar('aabb'))

print(firstUniqChar('loveleetcode'))

print(firstUniqChar('leetcode'))

