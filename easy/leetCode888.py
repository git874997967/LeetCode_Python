#888. Fair Candy Swap
 

def fairCandySwap(aliceSizes, bobSizes):
    sumA, sumB = sum(aliceSizes), sum(bobSizes)
     
    bobSizes = sorted(bobSizes)
    diff = (sumA - sumB) /2
    
    
    for a in aliceSizes:
        newNum = a - diff 
        start , end = 0, len(bobSizes) - 1
        while start + 1 < end:
            mid = (start + end) //2
            print(a,bobSizes[mid],newNum)
            if bobSizes[mid] == newNum :
                return [a, bobSizes[mid]]
            elif bobSizes[mid] > newNum :
                end = mid  
            else:
                start = mid  
        if bobSizes[start] == newNum :
            return [a,bobSizes[start]]
        elif bobSizes[end] == newNum :
            return [a,bobSizes[end]]
         
    return 

def fairCandySwap2(alice,bob):
    aSum, bSum  = sum(alice), sum(bob)
    B = set(bob)
    diff = (aSum - bSum) / 2
    for x in alice:
        if x + diff / 2 in B:
            return [x,bSum + diff / 2]

a0  = [69,31,57,7,16]


b0 = [4,85,14,38,33]


print(fairCandySwap(a0,b0)) # 1,2
 

 
