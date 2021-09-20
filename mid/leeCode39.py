#39. Combination Sum 
def combinationSum( candidates, target):        
    candidates.sort()
    result = []
    
    def backTracking(block,index,numSum):
        if numSum == target:
            return result.append(block[:])
        for idx1 in range(index,len(candidates)):
            if numSum > target: return 
            numSum += candidates[idx1]
            block.append(candidates[idx1])
            backTracking(block,idx1, numSum)
            numSum -= candidates[idx1]
            block.pop(-1)
          

    backTracking([],0,0)
    print(result)

combinationSum([2,3,6,7],7)


combinationSum([2,3,5,8],100)