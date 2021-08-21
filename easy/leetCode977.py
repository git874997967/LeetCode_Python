#977. Squares of a Sorted Array
 
def sortedSquares( nums):
     # two pointers
    start, end = 0, len(nums) - 1
    result = [0]* len(nums)
    pointer = end 
    while start <= end:
        numEnd , numStart = nums[end] **2, nums[start] ** 2
        if numStart <= numEnd:
            result[pointer] = numEnd
            end -= 1
        else:
            result[pointer] = numStart
            start += 1
        pointer -= 1
    print(result)
    return result 
sortedSquares([-4,-1,0,3,10])