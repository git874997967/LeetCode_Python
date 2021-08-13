def  findShortestSubArray(A):
    first, count , res, degree = {},{},0,0
    for i , a in enumerate(A):
        # remember the first apperance for each number
        first.setdefault(a,i)
        # remember the apperance time for each number
        count[a] = count.get(a,0) + 1
        if count[a] > degree:
            degree = count[a]
            res = i - first[a] + 1
        elif count[a] == degree:
            res = min(res, i - first[a] + 1)
    return res

   



findShortestSubArray([1,3,2,2,3,1])

findShortestSubArray([1,2,2,3,1,4,2])