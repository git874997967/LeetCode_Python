#1475. Final Prices With a Special Discount in a Shop
def finalPrices(prices):
    result = []
    start,lowPriceIndex = 0,1
    while start < len(prices) -1:
        while prices[lowPriceIndex] > prices[start] and lowPriceIndex < len(prices) -1:
            lowPriceIndex += 1
        if prices[start] >= prices[lowPriceIndex]:
            result.append(prices[start]- prices[lowPriceIndex])
        else:
            result.append(prices[start])
        start += 1
        lowPriceIndex = start + 1
    
    print(result + prices[lowPriceIndex - 1:])
    
    
    
finalPrices([8,4,6,2,3])
finalPrices([1,2,3,4,5])
finalPrices([10,1,1,6])
finalPrices([8,7,4,2,8,1,7,7,10,1])
finalPrices([4,7,1,9,4,8,8,9,4])