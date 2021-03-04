# 35. Search Insert Position
def searchInsert(self, nums, target):
    if ( lens(nums) ==0 )  or nums is None:
        return 0
    if target <= nums[0] :
        return 0
    if target >= nums[len(nums)-1]:
        return len(nums) 
    # start the binary search 
    start = 0 
    end = len(nums) -1 
    while start +1 < end:
        mid = ( start + end ) / 2
        if nums[mid] == target:
            return mid
        if  nums[mid] < target:
            start = mid
        if nums[mid ] > target:
            end = mid 
    return start + 1