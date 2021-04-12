# 231. Power of Two
def isPowerOfTwo(n):
    testNum = 1
    
    while testNum < 2 ** 31 - 1:
        if testNum -  abs(n) != 0:
            testNum = testNum << 1
        else:
            return True 
    return False 

print(isPowerOfTwo(-64))
## approach 2 
def isPowerOfTwo2(n):
      return False if n == 0 else n & (n - 1) == 0