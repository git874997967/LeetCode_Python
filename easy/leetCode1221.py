#1221. Split a String in Balanced Strings
def balancedStringSplit(s):
     
    result ,lCount,rCount = 0,0,0
    for char in s:
        if char == 'L':
            lCount += 1
        elif char =='R':
            rCount += 1
        if lCount == rCount:
            result += 1
            lCount = rCount = 0
    print(result)
    return result

balancedStringSplit("RLRRLLRLRL")


balancedStringSplit("RLLLLRRRLR")

balancedStringSplit("LLLLRRRR")


balancedStringSplit("RLRRRLLRLL")