# 374. Guess Number Higher or Lower
def guessNumber(n):
    start ,end = 1,n 
    while start + 1 < end :
        mid = start +( end -start) // 2
        if guessNumber(mid) == 0:
            return mid  
        elif guessNumber(mid) == 1:
            start = mid  
        else:
            end = mid 
    if guessNumber(start) == 0:
        return start
    return end