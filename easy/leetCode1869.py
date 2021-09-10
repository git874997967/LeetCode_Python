#1869. Longer Contiguous Segments of Ones than Zeros
def checkZeroOnes(s):
    if s == '1':
        return True 
    maxOne, maxZero = 0 , 0 
    i = 0 
    while i < len(s) - 1:
        j = i+ 1
        if s[i] == '1':
            oneLength, zeroLength = 1,0
        else:
            oneLength,zeroLength = 0,1
        while j < len(s) and s[j] == s[j - 1]:
            if s[j] == '1':
                oneLength += 1
                maxOne = max(maxOne,oneLength)
            else:
                zeroLength += 1
                maxZero = max(maxZero,zeroLength)
            j += 1
        i += 1
    print(maxOne,maxZero)
    return maxOne > maxZero


def checkZeroOnes2(s):
    if s == '1':
        return True
    curZero,curOne, maxZero,maxOne = 0 , 0, 0 , 0
    for char in s:
        if char == '1':
            curOne += 1
            maxZero = max(maxZero,curZero)
            curZero = 0
        else:
            curZero += 1
            maxOne = max(maxZero,curZero)
            curOne = 0
    return maxOne > maxZero


checkZeroOnes('1101')

checkZeroOnes('111000')

checkZeroOnes('1101000001111110')


