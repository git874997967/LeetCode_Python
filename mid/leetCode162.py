#162. Find Peak Element
# the nums size is larger than 0 so no empty need to take care
def findPeakElement(nums):
        left =0
        right = len(nums)-1
        while(left + 1 < right):
            mid = left +(right-left)//2 # Right biased mid as left = mid in else condition # prevent infinite loop
            if nums[mid] < nums[mid-1]: # False condition # Dec function # go left # Find Last False i.e the Last elem for which this condition will be False 
                right = mid 
            else: # decreasing so peak will be before mid or it can be mid
                left = mid
         
        return left if nums[left] > nums[right] else right

nums = []
print(findPeakElement(nums))

nums1 = [1]
print(findPeakElement(nums1))


nums2 = [3,2]
print(findPeakElement(nums2))

nums3 = [3,2,1]
print(findPeakElement(nums3))

nums3 = [1,2,3]
print(findPeakElement(nums3))

nums2 = [2,3]
print(findPeakElement(nums2))


 

 