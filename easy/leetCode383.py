# 383. Ransom Note
def canConstruct(ransomNote, magazine):
    dict = {}
    for char in ransomNote:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in magazine:
        if char in dict:
            dict[char] -= 1
        else:
            continue
    for count in dict.values():
        if count > 0:
            return False
    return True 

print(canConstruct("aa","aab"))

print(canConstruct("a","b"))


print(canConstruct("aa","ab"))

print(canConstruct("aa","sab"))