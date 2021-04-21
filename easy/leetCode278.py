# 278. First Bad Version
def firstBadVersion(n):
       start,end = 0, n 
       while start + 1 < end :
            mid = start +( end - start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
       if isBadVersion(start) :
            return start
       if isBadVersion(end):
            return end
       return -1
 
