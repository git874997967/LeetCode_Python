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


def summaryRanges2(nums):
    def f(num1 ,num2):
        return str(num1) if num1 == num2 else f'{num1}->{num2}'
    start , n = 0,len(nums)
    result = []
    
    while start < n :
        end = start  
        while end + 1 < n and  nums[end + 1] == nums[end] + 1:
            end += 1 
            
        
        result.append(f(nums[start], nums[end]))
        start = end + 1  
    print(result)
    return result    


summaryRanges2(nums2)