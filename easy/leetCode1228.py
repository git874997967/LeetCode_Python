#1228. Missing Number In Arithmetic Progression
def missingNumber(arr):
    diff = (max(arr) - min(arr) )//(len(arr))
    for i in range(min(arr),max(arr), diff):
        if i not in arr:
            print(i)
            return i 
    
missingNumber([5,7,11,13])
missingNumber([0,0,0,0,0])
missingNumber([15,13,12])