# 215. Kth Largest Element in an Array
import heapq
def findKthLargest( nums, k):
    # nums.sort(key = lambda x: x, reverse= True)
    # return nums[k - 1]
    # return heapq.nlargest(k,nums)[k-1]
      return heapq.nsmallest(len(nums) - k  + 1, nums)[-1]
arr = [1,3,5,6,2,4,8,0]
print(findKthLargest(arr,3))


 