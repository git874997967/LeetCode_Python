#1742. Maximum Number of Balls in a Box
def countBalls(lowLimit, highLimit):
    
    result = {}
    for num in range(lowLimit,highLimit+ 1):
        digSum = 0
        while num:
            reminder = num % 10
            digSum += reminder
            num = num // 10
        result[digSum] = result.get(digSum,0) + 1
    
    return max([v for v in result.values()])
    

print(countBalls(1,10))
print(countBalls(5,15))
print(countBalls(19,28))