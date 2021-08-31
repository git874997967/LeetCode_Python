#1426. Counting Elements
def countElements(arr):
    numMap = {}
    result = 0
    for num in arr:
        numMap[num] = numMap.get(num,0) + 1
    
    for k,v in numMap.items():
        if k+1 in numMap.keys():
            result += v
    return result


countElements([1,2,3])