#1704. Determine if String Halves Are Alike
def halvesAreAlike(s):
    str1,str2 = "",""
    for i in range(len(s)//2):
        if s[i] not in 'aeiouAEIOU':
            str1 += s[i]
        if s[i+ len(s)//2] not in 'aeiouAEIOU':
            str2 += s[i+ len(s)//2]
    return len(str1) == len(str2)