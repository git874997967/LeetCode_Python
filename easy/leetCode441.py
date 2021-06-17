# 441. Arranging Coins
def arrangeCoins(n):
     start, end = 1, n  
     while start + 1 < end:
         mid = (end - start) / 2 
         cur = mid * (mid + 1) / 2
         if cur == n:
             return mid
         if cur < n :
            start = mid 
         if cur > n:
            end = mid 
     return min(start,end)