# 605. Can Place Flowers edge detection
#  three adjancent 0 can place 1 flower
def canPlaceFlowers2(flowerbed, n):
        s = len(flowerbed)
        bed = [0] + flowerbed + [0]
        for i in range(1, s+1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                bed[i] = 1
                n -= 1
            if n <= 0: return True
        
        return False 

def canPlaceFlowers(flowerbed,n):
    i = 0 
    while(i < len(flowerbed)):
        if flowerbed[i] == 0:
            if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0: # the last place is 0 or the next is 0 both can be placed
                 n -= 1
                 i += 2
            else:
                i += 1
        return n < 1

print(canPlaceFlowers([1,0,0,0,1],1))

print(canPlaceFlowers([1,0,0,0,1],2))

print(canPlaceFlowers([1,0,0,0,0,1],2))

print(canPlaceFlowers([1,0,1,0,1,0,1],0))