# 628. Maximum Product of Three Numbers
# to find the max  two conditions 
# 1  all positive num  means max1 * max2 * max3
# 2 with negative must be two of them  min1 * min2 and the max1
def maximumProduct(nums):
    min1 = min2 = float('inf')
    max1 = max2 = max3 = float('-inf')     
    for num in nums:
        if num <= min1:
            min1, min2 = num, min1

        elif num <= min2:
            min2 = num 
        if num >= max1:
            max1 , max2, max3 = num, max1, max2
        elif num >=max2:
            max2,max3 = num , max2
        elif num >= max3:
            max3 = num 
    print(max1,max2,max3,min1,min2)
    return max(min1 * min2 * max1, max1 * max2 * max3) 

print(maximumProduct([-1,-2,-3]))
