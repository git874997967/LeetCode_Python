# 56. Merge Intervals
def merge( intervals):
    arr,result = [],[]
    intervals.sort(key = lambda x:x[0])
    temp = intervals[0]
    for i in range(1,len(intervals)):
        if temp[1] < intervals[i][0]: # cannot merge put the first into the result and current node become the temp
            result.append(temp)
            temp = intervals[i]
        else:
            # we can merge and cannot put the temp into the result 
            temp[1] = intervals[i][1] if intervals[i][1] > temp[1] else temp[1]
    result.append(temp)
    return result
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
print(merge(intervals))
print(merge(intervals2))


    

