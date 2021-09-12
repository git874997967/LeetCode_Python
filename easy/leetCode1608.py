#1608. Special Array With X Elements Greater Than or Equal X
import bisect
def specialArray(nums):

    nums.sort()
    for i in range(len(nums)+1):
        index = binarySearch(nums,i)
        print(index,i, index + i)
        if index + i == len(nums) :
            return i 

    return - 1


def binarySearch(nums, target):
     start, end  = 0, len(nums) - 1
     while start + 1 < end:
         mid = (start + end) // 2
         if nums[mid] >= target:
             end = mid  
         elif nums[mid] < target:
             start = mid 

     if nums[start] >=target :
         return start 
     if nums[end] >= target:
         return end 
     return len(nums)

     
            
   


# specialArray([3,5])



#print(specialArray([3,6,7,7,0]))

print(specialArray([3,9,7,8,3,8,6,6]))
