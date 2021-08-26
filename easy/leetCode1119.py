#1119. Remove Vowels from a String
def removeVowels(s):
    return s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')



print(removeVowels("leetcodeisacommunityforcoders"))
print(removeVowels("aeioukkkbcd"))