#1502. Can Make Arithmetic Progression From Sequence
def canMakeArithmeticProgression(arr):
    if len(arr) == 2 :
        return True 
    arr.sort()
    diff = arr[0] - arr[1]
    curNum = arr[0]
    for i in range(1,len(arr)):
        if arr[i] != curNum - diff:
            return False 
        curNum = arr[i]

    return True 


print(canMakeArithmeticProgression([3,5,1]))


print(canMakeArithmeticProgression([1,2,4]))