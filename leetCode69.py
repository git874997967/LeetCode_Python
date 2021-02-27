 # Sqrt(x)
 # binary search
 def mySqrt(self, x):
     if x<= 2: 
            return x
        start , end = 0, x//2
        while start + 1 < end:
            mid = (start + end ) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x :
                end = mid
            else:
                start = mid
        
        if end * end <= x:
            return end
        return start
# the best solution  Netwon method
# consider x is the area of one square  we want to find the length of the side 
# one side is L and the other side is A/L
# to make the rectangular as similar as the square we need to make two sides as close as possible
# the average is (L + A/L ) 2 use this until the area over the A( x )
def mySqrt(self, x):
    if x <= 2:
        return x
    x0 = x 
    x1 = (x0 + x / x0) /2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x/x0) /2
    return int(x1)
    
    
    
   if x <= 2:
       return x
   x0 = x 
   x1 = (x0 + x/ x0) /2
   while abs( x0 - x1) >= 1:
       x0 = x1
       x1 = (x0 + x/x0) /2 #  new iteration  the same format as logic outside of the while 
    return int(x1)