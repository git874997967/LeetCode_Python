import unittest
#1150. Check If a Number Is Majority Element in a Sorted Array
def isMajorityElement(nums, target):
    numMap = {}
    for num in nums:
        numMap[num] = numMap.get(num,0) + 1
        if numMap.get(target, 0 ) >  len(nums)// 2:
            return True 
    return False

# binary Search 
def isMajorityElement2(nums,target):
    left = self.searchLeft(nums,target)
    if left == -1:
        return False 
    right = self.searchRight(nums,target)
    return (right - left ) + 1 > len(nums) /2

def searchLeft(nums,target):
    start , end = 0 ,len(nums) -1
    while start + 1 < end :
        mid = (start + end) / 2
        if nums[mid] == target and  ( mid - 1 < 0  or nums[mid - 1] != target) :
            return mid 
        elif nums[mid] == target or nums[mid + 1] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    if nums[start] == target and nums[start - 1] != target:
        return start 
    if nums[end] == target and nums[end - 1] != target:
        return end 
    return -1

def searchRight(nums,target):
    start , end = 0 , len(nums) - 1
    while start + 1 < end:
        mid = (start + end) / 2
        if nums[mid] == target and (len(nums) == mid + 1 or nums[mid + 1] != target):
            return mid 
        elif nums[mid] == target or nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target :
            end = mid - 1


class UnitTest(unittest.TestCase):
  def test(self):
    result = isMajorityElement([2,5,5,],5)
    self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()   