#1399. Count Largest Group
def countLargestGroup(n):
    digitMap, maxSize,result = {}, float('-inf'),0
    for num in range(1,n +1):
        digitSum = 0
        while num:
            digit = num % 10
            digitSum += digit
            num = num // 10
        digitMap[digitSum] = digitMap.get(digitSum,0) + 1
        maxSize = max(digitMap.get(digitSum),maxSize)
    for k in digitMap.keys():
        if digitMap.get(k) == maxSize:
            result += 1
    print(result)
    return result




countLargestGroup(13)

countLargestGroup(2)
countLargestGroup(15)