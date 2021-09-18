#34. Find First and Last Position of Element in Sorted Array
def searchRange(nums,target):
    def binarySearch(nums,target):
         if len(nums) < 1:
             return -1
         start , end = 0, len(nums) - 1
         while start + 1 < end:
             mid = (start + end) // 2
             if nums[mid] == target:
                 return mid 
             elif nums[mid] < target:
                 start = mid 
             else:
                 end = mid 
         if nums[start] == target:
             return start
         elif nums[end] == target:
            return end 
         else:
             return -1
    index = binarySearch(nums,target)
    if index == -1: return [-1,-1]
    left = right = index 
    while left - 1 >= 0 and nums[left - 1] == target:
        left -= 1
    while right + 1 < len(nums) and nums[right + 1] == target:
        right += 1
    print([left,right])
    return [left,right]
    
 #      0 1 2 3 4 5 6 7  8  9
nums = [5,7,7,8,8,8,8,10,10,11]
searchRange(nums,7)# end = 1  1,2
searchRange(nums,8) # end = 3 3,4
searchRange(nums,10) # 5,6
searchRange(nums,1)