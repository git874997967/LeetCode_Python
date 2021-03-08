# 283. Move Zeroes
def moveZeroes(nums):
    zero = nonZero = 0
    for nonZero in range(len(nums)):
        
        if nums[nonZero]!= 0:# non replace
            nums[zero],nums[nonZero] = nums[nonZero],nums[zero]
            zero += 1
    return nums
arr = [0,1,0,1,0,3,12]
#print(moveZeroes(arr))

def moveZeroes2(nums):
    i = 0 
    n = len(nums)
    while i< len(nums):
        if nums[i] == 0:
            nums.pop(i) #The pop() method removes the item at the given index from the list and returns the removed item.
            nums.append(0)
        i += 1
    return nums
print(moveZeroes2(arr))
        