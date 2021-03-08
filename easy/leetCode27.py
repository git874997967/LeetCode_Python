# 27. Remove Element
def removeElements(nums, val):
    i = j = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

def  removeElements2(nums, val):
    i = j = 0
    for j in range( len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return nums