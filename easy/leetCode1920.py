#1920. Build Array from Permutation
def buildArray(nums):
     result = []
     for i in range(len(nums)):
         result.append(nums[nums[i]])
     print(result)
buildArray([5,0,1,2,3,4])

buildArray([0,2,1,5,3,4])


