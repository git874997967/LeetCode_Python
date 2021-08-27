#1180. Count Substrings with Only One Distinct Letter
def countLetters( s):
    total , left = 0 , 0 
    
    for right in range(len(s)+ 1):
        #  get the length
        if right == len(s) or s[right] != s[left]:
            subLength = right - left 
            total +=(1 + subLength) * subLength // 2
            left = right
    print(total)
    return total
    
def countLetters2(s):
    subLength , result = 1,0
    s = s + '0'
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            subLength += 1
        else:
            result, subLength = result + (1 + subLength)* subLength //2,1
    print(result)
    return result

def countLetters3(s):
    subLength, result = 1,0
    s = s + '0'
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            subLength += 1
        else:
            result,subLength = result + (subLength + 1) * subLength // 2, 1

countLetters2("aaaaabaaaa")