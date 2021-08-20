#917. Reverse Only Letters
def reverseOnlyLetters(s):
    s =  list(s)
    start, end = 0, len(s) - 1
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while start < end:
         
        while start < end and s[start] not in chars:
            start += 1
        while start < end and s[end] not in chars:
            end -= 1
        
        if start < end :
            s[start] ,s[end] = s[end],s[start]
            start += 1
            end -= 1
    print(''.join(s))
    return ''.join(s)


reverseOnlyLetters("ab-cd")

reverseOnlyLetters("a-bC-dEf-ghIj")

reverseOnlyLetters("Test1ng-Leet=code-Q!")
 



