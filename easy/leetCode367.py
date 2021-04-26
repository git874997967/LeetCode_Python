# 367. Valid Perfect Square
def isPerfectSquare(num):
    start ,end = 1,num  
    while start + 1 < end :
        mid = start + (end - start) // 2
        if mid * mid == num :
            return True
        elif mid * mid > num:
            end = mid 
        else:
            start = mid 
    if start * start == num or end * end == num :
        return True 
    return False 

print(isPerfectSquare(16))
print(isPerfectSquare(8))
print(isPerfectSquare(4))
print(isPerfectSquare(1))
print(isPerfectSquare(49))
print(isPerfectSquare(12))
print(isPerfectSquare(36))