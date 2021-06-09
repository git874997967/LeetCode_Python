# 448. Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
    result = []
    numSet = set(nums)
    for i in range(1,len(nums) + 1):
        if i not in numSet:
            result.append(i)
    return result


def findDisappearedNumbers2(nums):
    result = []
    for i in range(len(nums)):
        new_index = abs(nums[i]) - 1   
        if nums[new_index] > 0:
            nums[new_index] = -1 * nums[new_index]
    for i in range(len(nums)):
        if nums[i-1]> 0:
            result.append(i)

    return result



                


nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))

print(findDisappearedNumbers2(nums))