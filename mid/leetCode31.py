#31. Next Permutation
def nextPermutation(nums):
     if len(nums) <= 1:
         return nums
     i , j , k  = len(nums) -2, len(nums)-1, len(nums)-1;
     ##  take 12385764 as example  i points 6 , j k points 4
     # keep moving i, j pair forward if nums[i] <= nums[j]
     # now the i is 5 and j is 7
     while i >=0 and nums[i] >= nums[j]:
         i -= 1
         j -= 1
     # find out the num smaller than i move k forward
     if i >= 0:
         while nums[i] >= nums[k]:
             k -= 1
    # 4 is small than 5 and swap i,k  
         nums[i], nums[k] = nums[k], nums[i]
    # we also need to make the whole perm smallest  
    # so from j towards need to be revesed 
     nums[j:] = reversed(nums[j:])
     
     print(nums)
nums = [1,4,1]
nums = [4,1,1]
nextPermutation(nums)

