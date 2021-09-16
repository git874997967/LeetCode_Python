 #90. subsetsWithDup
def subsetsWithDup(nums):
     result = []
     nums.sort()
     used = [0] * len(nums)
     def backTracking(index, block,used):
         result.append(block[:])

         if index >= len(nums):
             return 

         for i in range(index,len(nums)):
             if not used[i]:
                 if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                     continue
             used[i] = 1
             block.append(nums[i])
             backTracking(i+1, block,used)
             block.pop(-1)
             used[i] = 0

     backTracking(0,[],used)
     print(result)
subsetsWithDup([1,2,2])