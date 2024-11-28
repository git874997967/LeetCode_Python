def countPairs(nums, target):
    result = 0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] < target:
                print(i,j)
                result += 1
                
    return result 

countPairs([-6,2,5,-2,-7,-1,3],  -2)