#1064. Fixed Point 
def fixedPoint(nums):
# binary search 
 start , end = 0 , len(nums) - 1
 while start + 1 < end:
     mid = (start + end) // 2 
     if nums[mid] == mid:
         end = mid 
     elif  nums[mid] < mid:
         start = mid
     elif nums[mid] > mid:
        end = mid 

 if nums[start] == start:
    return start
 elif nums[end] == end:
    return end
 return -1

print(fixedPoint([-10,-5,0,3,7]))

print(fixedPoint([0,2,5,8,17]))

print(fixedPoint([-10,-5,3,4,7,9]))