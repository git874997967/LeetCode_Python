# readBinaryWatch
from itertools import combinations
class Solution:
    def readBinaryWatch(self,num):
        result = []
        self.dfs(num,0,result)
        return result
    def dfs(self,num,hours,result):
        if hours > num:
            return 
        for hour in combinations([1,2,4,8],hours):
            hs = sum(hour)
            if hs > 12:
                continue
        for minu in combinations([1,2,4,8,16,32], num - hours):
            mins = sum(minu)
            if mins > 60:
                continue
            result.append("%d:%02d"% (hs,mins))
        self.dfs(num,hours + 1, result)

    
for i in combinations([1,2,4,8], 3):
    print(i)