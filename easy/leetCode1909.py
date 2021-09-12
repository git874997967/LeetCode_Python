#1909. Remove One Element to Make the Array Strictly Increasing
def canBeIncreasing(nums):
     minCount,maxCount = 0 , 0 
     start ,end = 0, len(nums) - 1
     minNum = float('inf')
     maxNum = float('-inf')
     while end >= 0:
         if nums[end] < minNum:
             minNum = nums[end]
         else:
             minCount += 1
         end -= 1
     while start <= len(nums) - 1:
         if nums[start] >maxNum:
             maxNum = nums[start]
         start += 1

     if minCount > 1 and maxCount > 1:
         return False
     return True 

print(canBeIncreasing([1,2,10,5,7]))
print(canBeIncreasing([1,2,3]))
print(canBeIncreasing([105,924,32,968]))



