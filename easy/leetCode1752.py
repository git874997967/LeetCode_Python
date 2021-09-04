#1752. Check if Array Is Sorted and Rotated
def check( nums):
    lenNums,newNums = len(nums),nums * 2
    nums.sort()
    for i in range(len(nums)+1):
        #  1 2 3 4 5 len = 5 index 0 4
        print(newNums[i:i+ lenNums])
        if newNums[i:i +lenNums] == nums:
            return True 

    return False

print(check([3,4,5,1,2]))