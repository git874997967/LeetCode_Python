# 697. Degree of an Array (mid) 
def findShortestSubArray(nums):
    maxDegree, result, degreeCandidate ,degreeMap = 0 ,len(nums), {}, {}
    
    for index in range(len(nums)):
        num = nums[index] 
        # update the first index and count = 1
        if num not in degreeMap:
            loc = [0,0]
            loc[0] = index 
            degreeCandidate[num] = loc 
            degreeMap[num] = 1
        # update the laste index   and count + 1
        else:
            loc = degreeCandidate[num]
            loc[1] = index 
            degreeCandidate[num] = loc
            degreeMap[num] += 1
        
        maxDegree = max(maxDegree, degreeMap[num])
    if maxDegree == 1:
        return 1
    for key in degreeMap.keys():
        if degreeMap[key] == maxDegree:
          
            dis = degreeCandidate[key][1] - degreeCandidate[key][0] + 1
            result = min(dis, result)
    return result



def  findShortestSubArray2(A):
    first,count, res, degree = {} , {}, 0, 0
    for i , a in enumerate(A):
        first.setdefault(a,i)
        #  use get(a,0) + 1 to init the dict count 
        count[a] = count.get(a,0) + 1
        if count[a] > degree:
            degree = count[a]
            res = i - first[a] + 1
        elif count[a] == degree:
            res = min( res , i - first[a] +1 )  
        
    return res
 
 

print(findShortestSubArray([1,3,2,2,3,1]))

print(findShortestSubArray([1,5,2,3,5,4,5,6]))

print(findShortestSubArray([2,1]))

    
