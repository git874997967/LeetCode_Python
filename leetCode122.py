# 122. Best Time to Buy and Sell Stock II
def maxProfit(self, prices):
    max = 0 
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            max += prices[i] - prices[i - 1]
    return max