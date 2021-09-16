 #78. Subsets
def subsets(nums):
     result = []
     nums.sort()
    
     def backTracking(index, block):
         result.append(block[:])

         if index >= len(nums):
             return 

         for i in range(index,len(nums)):
             block.append(nums[i])
             backTracking(i+1, block)
             block.pop(-1)

     backTracking(0,[])
     print(result)
subsets([1,2,2])