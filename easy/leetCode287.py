#287. Find the Duplicate Number
## as the number is from [1,n] and we will use the index to store them  
## nums[0] as no num is 0 and we will store the actual num at nums[0]
## and each run will kind of sort the num with its index
def findDuplicate(nums):
      while nums[0] != nums[nums[0]]:
          nums[nums[0]] , nums[0] = nums[0],nums[nums[0]]
          print(nums)
      return nums[0]


## we filp the num one we visited it  
## if we have dup means we will see it again and that is filped 
def findDuplicate2(nums):
    for num in nums:
        cur = abs(num)
        if num[cur] < 0:
            return cur 
        nums[cur] *= -1

findDuplicate([2,2,2,2])


findDuplicate2([1,3,4,2,2])

 