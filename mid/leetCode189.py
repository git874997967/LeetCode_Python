def rotate(array,index):
    if len(array)< index:
        return
    array = array[::-1] 
    return array[len(array) - index::-1] + array[:len(array) - index:-1]

index,array  = 3, [1,2,3,4,5,6,7,8,9,10]
print(rotate(array,index))


def rotate2(nums,k):
    if len(nums)< k:
        return
    k %= len(nums)
    reverse(nums,0, len(nums) -1)
    reverse(nums, 0, k - 1)
    reverse(nums,k, len(nums) - 1)

def reverse(nums, start,end):
    while start< end:
        nums[start] ,nums[end] = nums[end],nums[start]
        start,end = start + 1, end - 1

