#1056. Confusing Number
def confusingNumber(n):
    numMap = {}
    x = n
    reversed =  0
    for i in range(10):
        if i in (0,1,8):
            numMap[i] = i
        elif i == 6:
            numMap[i] = 9
        elif i == 9:
            numMap[i] = 6
    while n > 0:
        digit = n % 10
        n = n / 10
        if numMap.get(digit,11) == 11:
            return False 
        
        reversed  = reversed * 10 + numMap.get(digit)
        
    return reversed != x


print(confusingNumber(0))
print(confusingNumber(10010))
print(confusingNumber(10801))
print(confusingNumber(916))
print(confusingNumber(25))
print(confusingNumber(6))
print(confusingNumber(10301))
print(confusingNumber(88))