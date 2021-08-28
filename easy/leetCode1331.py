#1331. Rank Transform of an Array
def arrayRankTransform(arr):
    sortArr = sorted(arr)
    numSet = set(sortArr)
    result, numMap =[], {}
    print(numSet)
    for i,num in enumerate(numSet):
        numMap[num] = i + 1

    for i in range(len(arr)):
        result.append(numMap.get(arr[i]))
    print(result)


arrayRankTransform([4,1,3,2])

arrayRankTransform([10,10,10])


