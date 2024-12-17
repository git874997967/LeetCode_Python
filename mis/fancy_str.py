def  fancy(str):
    result = s[0:2]
    i = 2 
    if len(s) < 3:
        return s 
    else:
        while i < len(s):
            if s[i] == result[-1] == result[-2]:
                i += 1
            else:
                result += s[i]
                i += 1 
                
        return ''.join(result)
    
    
def fancy2(str):
    count = 0
    ans = []
    tmp = str[0]
    for c in s:
        if c != tmp:
            count = 1
            tmp = c
        else:
            count += 1
        if count < 3:
            ans.append(c)
            
    return ''.join(ans)