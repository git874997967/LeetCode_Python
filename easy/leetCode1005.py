#1005. Maximize Sum Of Array After K Negations
# need to take the k with length of negNum
def largestSumAfterKNegations(nums, k):
    
     nums = sorted(nums)
     result , negNum, posNum = 0, [i for i in nums if i < 0 ], [i for i in nums if i >= 0]
     print(negNum,posNum)
     if len(negNum) == 0:
         return sum(posNum) if k % 2 == 0 else sum(posNum) - posNum[0] * 2
     elif len(posNum) == 0:
         if k < len(negNum):
             for num in negNum:
                 if k >0:
                     result += abs(num)
                     k -= 1
                 else:
                     result += num 
                 return result
         else:
            
            return sum([abs(i) for i in negNum]) if (k - len(negNum)) %2 == 0 else sum([abs(i) for i in negNum]) + negNum[-1] * 2
    # negNum is not None and posNum is not None
     elif k < len(negNum):
          
         for num in negNum:
             print(num, abs(num),result)
             if k > 0 :
                 result += abs(num)
                 k -= 1
             else:
                 result += num 
             
         return  result + sum(posNum)
     else:
         return sum([abs(i) for i in nums]) - min(posNum[0], abs(negNum[-1])) * 2 if  (k - len(negNum)) %2  == 1 else sum([abs(i) for i in nums]) 


print(largestSumAfterKNegations([2,-3,-1,5,-4],2)) # 13

print(largestSumAfterKNegations([3,-1,0,2],3))

print(largestSumAfterKNegations([4,2,3],1))

print(largestSumAfterKNegations([5,6,9,-3,3],2))

print(largestSumAfterKNegations([1,3,2,6,7,9],3))



print(largestSumAfterKNegations([-4,-2,-3],4))


 
                    
        
        