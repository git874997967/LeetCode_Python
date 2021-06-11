# 507. Perfect Number
# while for loop is fater than the while
def checkPerfectNumber(num):
    if num == 1 or num == 2:
        return False
    start,sum = 2, 0
    root = int(num ** 0.5)
    while start <= root: 
        if num % start == 0:
            if start != num // start:
                sum = start + num // start + sum 
            else :
                sum + start
        start += 1
    return True if  sum + 1 == num else False

print(checkPerfectNumber(1))

print(checkPerfectNumber(2))

print(checkPerfectNumber(34))

print(checkPerfectNumber(28))