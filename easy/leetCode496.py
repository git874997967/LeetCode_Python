# 496. Next Greater Element I (mid)
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
def nextGreaterElement(nums1, nums2):
    result ,monStack, numMap = [], [], {}
    for i in range(len(nums2)):
        # if the num larger than the stack head then keep poping into the map
        while len(monStack) > 0 and nums2[i] > monStack[-1]:
            numMap[monStack.pop()] = nums2[i]
        # if not then add the num in the stack
        monStack.append(nums2[i])
    # there is no larger number than the stack  just put -1
    while len(monStack) > 0:
        numMap[monStack.pop()] = -1
    for i in range(len(nums1) ):
      result.append(numMap.get(nums1[i]))
    return result

num1 =[4,1,2]
num2 = [1,3,4,2]
print(nextGreaterElement(num1,num2))
