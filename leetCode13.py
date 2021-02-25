#13. Roman to Integer
# count from back to front and use map
def romanToInt(str):
    result = 0 
    if len(str) == 0 or (str is Null):
        return 0
    numDict = {
                      'I' : 1,
                       'V' : 5,
                       'X' : 10,
                       'L' : 50,
                       'C' : 100,
                       'D' : 500,
                       'M' : 1000
    }
    result = 0
    while i < len(str) - 1:
        if(numDict[s[i]] >= numDict[s[i+1]]):
            result += numDict[s[i]]
            i += 1
        else:
            result += numDict[s[i+1]] - numDict[s[i]]
            i += 2
    res += numDict[s[i]]
    return result

# solution 2 
# introduce 2 pointers( cur and prev and check the relationship  with two size sliding window.)
def romanToInt(str):
    numDict = {
                      'I' : 1,
                       'V' : 5,
                       'X' : 10,
                       'L' : 50,
                       'C' : 100,
                       'D' : 500,
                       'M' : 1000
    }
    if len(str) == 0 : return 0
    result = index = prev = cur = 0 
    while index < len(str):
        cur = numDict[str[index]]
        if cur > prev:
            result += cur - prev * 2
        else:
            result += cur
        prev = cur
        index += 1
    return result