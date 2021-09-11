# 35. Search Insert Position
def searchInsert(nums, target):
    nums.sort()
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            end = mid 
        elif nums[mid] < target:
            start = mid 
    if nums[start] >= target:
        return start 
    elif nums[end] >= target:
        return end 
    return end + 1