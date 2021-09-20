#40. Combination SumII
def combinationSumII( candidates, target):
    result = []
    candidates.sort()
    def backTrack(index, numSum, block):
            if numSum == target:
                return result.append(block[:])
            for idx1 in range(index, len(candidates)):
                if numSum + candidates[idx1] > target: return 
                if idx1 > index and candidates[idx1] == candidates[idx1-1] :
                    continue
                    
                numSum += candidates[idx1]
                block.append(candidates[idx1])
                backTrack(idx1 + 1, numSum, block)
                numSum -= candidates[idx1]
                block.pop(-1)

    backTrack(0,0,[])
    print(result)
    return result

combinationSumII([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27) 