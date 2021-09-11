#1608. Special Array With X Elements Greater Than or Equal X
def specialArray(nums):
    nums.sort()
    for i in range(len(nums)+1):
        index = binarySearch(nums,i)
        print(index,i, index + i)
        if index + i == len(nums) :
            return i 

    return - 1


def binarySearch(nums, val):
        low, high = 0, len(nums)
        while low < high:
            mid = low +  (high - low) // 2
            if nums[mid] >= val:
                high = mid
            else:
                low = mid + 1
        
        return low


# specialArray([3,5])



print(specialArray([3,6,7,7,0]))