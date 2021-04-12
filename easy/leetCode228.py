# 228. Summary Ranges
def summaryRanges( nums):
    result = []
    resultStr = []
    if not nums:
        return result 
    arr = [nums[0]]
    for num in range(1,len(nums)):
        # if continus then update the current range 
        if nums[num] == arr[-1] + 1 :
            arr.append(nums[num])
        # finish the range and create a new range 
        else :
             arr = [arr[0],arr[-1]]
             result.append(arr)
             arr = [nums[num]]
    result.append(arr)
    for arr in result:
        if arr[0] == arr[-1]:
            resultStr.append( str(arr[0]))
        else:
            resultStr.append(str(arr[0]) +"->"+ str(arr[-1]))
    print(resultStr)
    return result 
nums = [0,2,3,4,6,8,9]
nums2 = [0,1,2,4,5,7]
summaryRanges([-1])
summaryRanges([])
summaryRanges(nums)
summaryRanges(nums2)