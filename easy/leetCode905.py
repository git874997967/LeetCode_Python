# 905. Sort Array By Parity
def sortArrayByParity2(nums):
    moveBack, moveForward = 0,0 
    # locate the first odd Number to move back
    while moveForward != len(nums) - 1 and moveBack != len(nums) - 1:
        while nums[moveBack] % 2  == 0  :
            moveBack += 1
            if moveBack == len(nums):
                return nums
        moveForward = moveBack
        while nums[moveForward] % 2 != 0  :
            moveForward += 1
            if moveForward == len(nums):
                return nums
        nums[moveBack], nums[moveForward]  = nums[moveForward], nums[moveBack]
 
    return nums

def sortArrayByParity(nums):
    if len(nums) <= 1:
        return nums
    findOdd, findEven = 0, len(nums)- 1
    while findOdd < findEven :
        while findOdd < findEven and nums[findOdd] % 2 == 0 :
            findOdd += 1
        while findOdd < findEven and nums[findEven] %2 == 1:
            findEven -= 1
        if findEven != findOdd:
            nums[findOdd], nums[findEven] = nums[findEven],nums[findOdd]
    print(nums)
    return nums 
    


sortArrayByParity2([1,3,2,4,5,6])
sortArrayByParity2([2,3,1,4,6,7,54])# 2,4,6,
sortArrayByParity2([1,3,65,7,9,2,4,6,8,100,102])
sortArrayByParity2([0])
sortArrayByParity2([0,2])


