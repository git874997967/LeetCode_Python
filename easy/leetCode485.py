# 485. Max Consecutive Ones
def findMaxConsecutiveOnes( nums):
   s= "".join(str(elm) for elm in nums)
   maxLen = 0
   for i in s.split("0"):
       curLen = len(i)
       maxLen = max(len(i), maxLen)
   return maxLen


def findMaxConsecutiveOnes2(nums):
    i = finalLength = length = 0
    while i < len(nums):
        if nums[i] == 1:
            length += 1
            finalLength = max(finalLength,length)
        else:
            finalLength = max(finalLength, length)
            length = 0
        i += 1
    return finalLength


print(findMaxConsecutiveOnes2([1,1,0,1,1,1]))