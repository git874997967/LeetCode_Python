#77. Combinations
def combine(n, k):
      
      result = []
      def backTrack (index, block):
          if len(block) == k:
              return result.append([i for i in block])

          for i in range(index,n - k + len(block) + 2):
              block.append(i)
              backTrack(i + 1, block)
              block.pop(-1)
      
      backTrack(0,[])
      print(result)
      return result 
combine(5,2)