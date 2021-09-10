#1848. Minimum Distance to the Target Element
def getMinDistance(nums, target, start):
    if nums[start] == target:
        return start 
     
    result = len(nums)
    for i in range(len(nums)):
        if nums[i] == target:
            result = min(result,abs(i- start))

    return result