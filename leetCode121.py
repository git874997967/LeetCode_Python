# 121. Best Time to Buy and Sell Stock
def maxProfit(self, prices):
    if len(prices) == 1 :
        return 0
    minPrice , maxPrice = prices[0], 0
    for i in range(len(prices)):
        minPrice = min(prices[i],minPrice)
        maxPrice = max(prices[i] - minPrice, maxPrice)
    return maxPrice 