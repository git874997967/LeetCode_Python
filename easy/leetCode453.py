# 453. Minimum Moves to Equal Array Elements
#  add n-1 number with 1 equal to minus 1 to only number   
#  and then the question become to  how to make all number to minum   
#  then just sum up all the diff between nums[n] and nums min  
#  then that will work 
# in a nut shell  result = sum(nums) - min(nums) * len(nums)
def minMoves(nums):
    nums.sort()
   
    count = 0 
    for i in range(len(nums)):
        count += nums[i] - nums[0]
    return count

def minMoves(nums):
    return sum(nums) - min(nums) * nums.length
nums =[13,18,3,10,35,68,50,20,50]
print(minMoves(nums))
