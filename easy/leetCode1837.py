#1837. Sum of Digits in Base K
def sumBase(n, k):
    result = 0
    while n :
        remind = n % k
        result += remind 
        n = n // k 
    return result

sumBase(34,6)

