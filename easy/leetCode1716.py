#1716. Calculate Money in Leetcode Bank
def totalMoney(n):
    wholeWeek = n // 7 
    reminDays = n % 7 
    result = 0
    
    for i in range(wholeWeek):
        result += 28
        result += i * 7
    reminStart = 1 + wholeWeek
    for i in range(reminDays):
        result += reminStart
        reminStart += 1

    print(result,reminStart)     
totalMoney(4)
totalMoney(10)
totalMoney(20)