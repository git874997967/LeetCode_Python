#1356. Sort Integers by The Number of 1 Bits
from typing import DefaultDict
def sortByBits(arr):
    result = []
    charDict = DefaultDict(list)
    for num in arr:
        strNum = bin(num)
        oneTimes = strNum.count('1')
        charDict[oneTimes].append(num)
        print(num, strNum, oneTimes)

    sorted(charDict.items(), key = lambda x:(x[0]))
    for i in charDict.values():
        i.sort()
        result += i
    print(result)
    return charDict

sortByBits([1024,512,256,128,64,32,16,8,4,2,1])
sortByBits([10,100,1000,10000])
