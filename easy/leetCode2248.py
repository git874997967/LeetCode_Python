def intersection(nums):
    count_map = {}
    result = []
     
    for num in nums:
        for i in num:
            count_map[i] = count_map.get(i,0) + 1
            if count_map[i] == len(nums):
                result.append(i)
                
    print(sorted(result))
    


intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])
        