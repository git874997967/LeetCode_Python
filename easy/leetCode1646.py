#1646. Get Maximum in Generated Array
def getMaximumGenerated(n):
    arr  = []
    arr.append(0)
    arr.append(1) 
    
    for i in range(2, n+ 1):
        print(i)
        if i % 2 == 0:
            arr.append(i // 2) 
        else:
            arr.append(arr[(i+1)//2] + arr[(i -1)//2])
    return max(arr) if n >= 1 else 0
getMaximumGenerated(7)
getMaximumGenerated(2)
getMaximumGenerated(3)
