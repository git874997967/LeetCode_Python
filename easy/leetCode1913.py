#1913. Maximum Product Difference Between Two Pairs
def maxProductDifference(nums):
     minNum, subMin, maxNum, subMax = float('inf'),float('inf'), float('-inf'), float('-inf')
     for num in nums:
         if num > maxNum:
             maxNum, subMax = num , maxNum 
         elif num > subMax:
             subMax = num 
         if num < minNum:
             minNum, subMin = num, minNum
         elif num < subMin:
             subMin = num
     return maxNum * subMax - minNum * subMin        