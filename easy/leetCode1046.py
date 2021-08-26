#1046. Last Stone Weight
import heapq
def lastStoneWeight( stones):
    heapq._heapify_max(stones) 
    
    while len(stones) > 1:
        maxStone = heapq._heappop_max(stones)
        secStone = heapq._heappop_max(stones)
        if maxStone >= secStone:
            heapq.heappush(stones, maxStone - secStone)
        heapq._heapify_max(stones)
         
    print(stones[0])
     
lastStoneWeight([2,7,4,1,8,1])


# lastStoneWeight([1])
# lastStoneWeight([1,1])