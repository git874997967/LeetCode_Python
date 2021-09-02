#1566. Detect Pattern of Length M Repeated K or More Times
def containsPattern(arr, m, k):
    if m == len(arr):
        return True if k == 1 else False 
    patternMap = {}
    for i in range(len(arr) - m+1):
        pattern = arr[i:i+ m]
        print(arr[i:i+ m], pattern * k)
        if pattern * k == arr[i:i+ m * k]:
            return True
    return False 

arr = [1,2,4,4,4,4]
m = 1
k = 3
arr = [1,2,1,2,1,1,1,3] 
m = 2
k = 2
arr = [1,2,1,2,1,3]
m = 2 
k = 3

arr = [3,2,2,1,2,2,1,1,1,2,3,2,2]
m = 3
k = 2
print(containsPattern(arr,m,k))