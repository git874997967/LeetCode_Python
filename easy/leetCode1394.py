#1394. Find Lucky Integer in an Array
def findLucky(arr):
    numMap,candidateNumber = {},[]
    for num in arr:
        numMap[num] = numMap.get(num,0) + 1
    print(numMap)
    for k,v in numMap.items():
        if k == v:
            candidateNumber.append(k)
    return max(candidateNumber) if len(candidateNumber) > 0 else -1

findLucky([2,2,3,4])