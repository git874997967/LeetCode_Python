#1217. Minimum Cost to Move Chips to The Same Position
def minCostToMoveChips(position):
     coinsArr = [0] * 2
     for pos in position:
         if pos % 2 == 0 :
             coinsArr[0] += 1
         else:
             coinsArr[1] += 1
      
     print(coinsArr[0],coinsArr[1])
     return min(coinsArr[0],coinsArr[1])


minCostToMoveChips([1,2,3])

minCostToMoveChips([1,1000000000])
minCostToMoveChips([2,2,2,3,3])