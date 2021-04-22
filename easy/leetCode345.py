# 345. Reverse Vowels of a String
def reverseVowels(s):
    if not s: 
        return s  
    sList = [ char for char in s ]
    start , end = 0, len(s) - 1 
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    while start < end:
        if sList[start] in vowels and sList[end] in vowels: 
            
            sList[start],sList[end] = sList[end],sList[start]
            start += 1
            end -= 1
        elif sList[start] in vowels and sList[end] not in vowels:
            end -= 1
        elif sList[start] not in vowels and sList[end] in vowels:
            start += 1
        else:
            start += 1
            end -= 1
     
    return str(sList)

reverseVowels("hello")

reverseVowels("leetcode") 
