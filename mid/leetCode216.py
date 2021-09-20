#216. Combination Sum III
def combinationSum3(k, n):
     arr = [i for i in range(1,10)]
     result = []
     def backTrack(numSum , block,index):
         if numSum == n and len(block) == k:
            result.append(block[:])
         for idx in range(index, len(arr)):
             if numSum > n or len(block) > k: return 
           
             numSum += arr[idx]
             block.append(arr[idx])
             backTrack(numSum, block, idx + 1)
             numSum -= arr[idx]
             block.pop(-1)

     backTrack(0,[],0)
     print(result)

combinationSum3(4,1)
combinationSum3(3,9)
combinationSum3(3,7)
combinationSum3(9,45)
