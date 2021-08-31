#1464. Maximum Product of Two Elements in an Array
def maxProduct(nums):
    firstMax = secMax = float('-inf')
    for num in nums:
        if num > firstMax:
            firstMax, secMax  = num, firstMax
        elif num > secMax:
            secMax = num
     
    return (firstMax - 1) * (secMax - 1)