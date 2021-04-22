# 344. Reverse String
def reverseString(s):
    if not s:
        return s 
    for index in range((len(s)//2)):
        s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index] ,s[index]

    return s 

s = ["h","e","l","l","o"]
reverseString(s)