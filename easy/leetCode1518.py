#1518. Water Bottles
def numWaterBottles(numBottles, numExchange):
    result = numBottles
    while numBottles >= numExchange:
       
        nextFull = numBottles // numExchange
        numEmpty = numBottles % numExchange
        numBottles = nextFull + numEmpty
        result += nextFull
    
    print( result )


numWaterBottles(9,3)
numWaterBottles(5,5)
numWaterBottles(15,4)
numWaterBottles(2,3)