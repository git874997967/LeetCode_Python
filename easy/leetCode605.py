# 605. Can Place Flowers
#  three adjancent 0 can place 1 flower
def canPlaceFlowers(flowerbed, n):
        s = len(flowerbed)
        bed = [0] + flowerbed + [0]
        for i in range(1, s+1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                bed[i] = 1
                n -= 1
            if n <= 0: return True
        
        return False 

print(canPlaceFlowers([1,0,0,0,1],1))

print(canPlaceFlowers([1,0,0,0,1],2))

print(canPlaceFlowers([1,0,0,0,0,1],2))

print(canPlaceFlowers([1,0,1,0,1,0,1],0))