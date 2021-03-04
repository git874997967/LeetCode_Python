# 121. Best Time to Buy and Sell Stock
def maxProfit(self, prices):
    if len(prices) == 1 :
        return 0
    minPrice , maxPrice = prices[0], 0
    for i in range(len(prices)):
        minPrice = min(prices[i],minPrice)
        maxPrice = max(prices[i] - minPrice, maxPrice)
    return maxPrice 
##  状态转移方程 
## 第i天卖掉盈利为 fi  第 i+1 天卖掉盈利为  fi - a[i-1] +a[i]
def maxProfit2(self,prices):
    localMax = finalMax = 0
    for i in range(1,len(prices)):
        localMax = max(localMax + prices[i] - prices[i - 1], 0)
        finalMax = max(localMax , finalMax)
    return finalMax