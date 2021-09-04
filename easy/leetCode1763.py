#1763. Longest Nice Substring
def longestNiceSubstring(s):
    result,maxLen = "",0
    if len(s) == 1:
        return s
    for i in range(len(s)):
        
        for j in range(i+1,len(s)+1):
             nice = 0
             strSet = set(s[i:j])
             
             for char in s[i:j]:
                 if char.lower() in strSet and char.upper() in strSet:
                     nice += 1
                     
                 else:
                    
                     break
             if nice == len(s[i:j]) and nice > maxLen:
                 maxLen = nice 
                 result = s[i:j]
                

    print(result)
longestNiceSubstring("yazaAaY")
longestNiceSubstring("bB")
longestNiceSubstring("c")
longestNiceSubstring("dDzeE")

