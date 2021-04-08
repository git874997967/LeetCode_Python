# 172. Factorial Trailing Zeroes

def trailingZeroes(self, n):
    zero_count = 0 
    while n > 0:
        n = n // 5 
        zero_count += n 
    return zero_count
        