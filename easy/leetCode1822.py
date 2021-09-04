#1822. Sign of the Product of an Array
def arraySign(nums):
    prod = 1
    for num in nums:
        prod *= num
        if num == 0 :
            return 0
    return 1 if prod > 0 else -1