def maxProfit(prices):
     f1 = f2 = f3 = f4 = float('-inf')
     for price in prices:
         f1 = max(f1,-price) # buy means the the cost we need to have the cost 
         f2 = max(f2, f1 + price)
         f3 = max(f3, f2 - price) # 2nd buy to have the cost
         f4 = max(f4, f3 + price)
     print(f4)
     return f4
    
maxProfit([3,3,5,0,0,3,1,4])       
    
    