#1979. Find Greatest Common Divisor of Array
def findGCD(nums):
    def gcd(a,b): # min, max 
        if b % a == 0:
            return a 
        return gcd(b % a,a)
    return gcd(min(nums),max(nums))
