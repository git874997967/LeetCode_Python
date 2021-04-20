# 278. First Bad Version
def firstBadVersion(n):
    if n == 1:
        return n 
  
    start = 0
    while start +1 < n :
        mid = n / 2
        if isBadVersion(mid):
    #  the first bad in 0 ... mid  
            start = mid  
        else:
    # the first bad in mid... n 
            n = mid
    return start if isBadVersion(start) else mid 

print(firstBadVersion(5)) 

