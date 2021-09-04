#1708. Largest Subarray Length K
def largestSubarray(nums, k):
     
    sortNums = sorted(nums,reverse= True)
    maxNum = sortNums[0]
    if k == 1:
        return [sortNums[0]]
    if len(nums) - nums.index(maxNum) >= k:
        startInd = nums.index(maxNum)
        return nums[startInd:startInd + k]
    else:
        while len(nums) - nums.index(maxNum) < k:
            maxNum = sortNums.pop(0)

        startInd = nums.index(maxNum)
        return nums[startInd:startInd + k]

def largestSubarray(nums, k):
    idx =  nums.index(max(nums[:len(nums)-k+1])) 
    return nums[idx:idx+k]


 
print(largestSubarray([1,4,5,2,3,5,3,5,5],2))
print(largestSubarray([12,44,56,66,27,38,5,79],6))
print(largestSubarray([152319089,905035065,375858120,916819602,568374582,388725585,371065667,178426493,742412571,889260814,512431401,438590275,391136964,934060090,898314186,185191490,739096184,556347984,930903528,213302248,792236082,303716676,990347766,358994042,482951961],
21))
