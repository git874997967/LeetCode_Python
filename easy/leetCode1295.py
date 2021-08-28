#1295. Find Numbers with Even Number of Digits
import math
def findNumbers(nums):
    result = 0
    for num in nums:
        lg10 = int(math.log10(num)) 
        result += 1 if lg10 % 2 == 1 else 0
    print(result)
    return result

        

findNumbers([1,3,200,435,3242,2342133,43])
findNumbers([555,901,482,1771])
findNumbers([12,345,2,6,7896])
