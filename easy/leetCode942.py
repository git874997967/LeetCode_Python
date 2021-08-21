#942. DI String Match
def diStringMatch2(s):
    n , numSet,result = len(s), set(),[]
     
    if s[0] == 'I':
        result.append(0)
        numSet.add(0)
    elif s[0] == 'D':
        result.append(n)
        numSet.add(n)
    for i in range(0,n):
        num = result[i- 1]
        if s[i] == 'I':
            while num in numSet:
                num += 1
         
        elif s[i] == 'D':
            while num in numSet:
                num -= 1
         
        numSet.add(num)
        result.append(num)
    minNum = min(result)
    
    result = [i - minNum for i in result]
      
    return result 

def diStringMatch(s):
    low,high = 0,len(s)
    result = []
    for x in s:
        if x == 'I':
            result.append(low)
            low += 1
        else:
            result.append(high)
            high -= 1
    print(result ,[low])
    return result + [low]

diStringMatch("IDID")

diStringMatch("III")

diStringMatch("DDI")