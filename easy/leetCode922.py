#922. Sort Array By Parity II
def sortArrayByParityII( nums):
     odd = 1 
     for even in range(0,len(nums),2):
         # find the even index but with odd number
         if nums[even] % 2  :
             # find the odd index but with the even number
            while nums[odd] % 2 :
                odd += 2
            nums[odd] , nums[even] = nums[even], nums[odd]

     print(nums)
     return nums 

 

sortArrayByParityII([3,2,0,1])

sortArrayByParityII([4,2,5,7])

sortArrayByParityII([0,1])

sortArrayByParityII([3,2])

sortArrayByParityII([2,3,1,1,4,0,0,4,3,3])


sortArrayByParityII([0,0,1,1,2,3,3,3,4,4])


sortArrayByParityII([1,3,5,7,9,2,4,6,8,0])

sortArrayByParityII([1,2,3,4,5,6,7,8,9,0])
