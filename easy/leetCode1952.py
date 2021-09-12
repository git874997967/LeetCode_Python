#1952. Three Divisors
def isThree(n):
    if n == 1: return False
    sqrt = int(n ** 0.5)
    if sqrt ** 2 == n:
        for i in range(2,sqrt):
            print(i, sqrt,)
            if n % i == 0:
                return False 
    else:
        return False
    return True