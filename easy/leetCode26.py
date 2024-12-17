# 26. Remove Duplicates from Sorted Array
# that is better call re-arrange array rather than remove  ( move duplidate to the end) 
#  trigger move operation once the element are diff  ( means  skip the same elements)
def removeDuplicates(nums):
     if len(nums) <= 1:
         return len(nums)
     p1 = p2 = 0
     for p2 in range(len(nums)):
         if nums[p2] != nums[p1]:
             p1 += 1
             nums[p1] = nums[p2]
     return p1 + 1

def removeValue( nums, val):
    p1 = p2  = 0
    for p2 in range( len(nums)):
        if nums[p2] != val:
           nums[p1] = nums[p2]
           p1 += 1
           
           
           