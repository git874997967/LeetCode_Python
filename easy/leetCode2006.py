#Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
def countKDifference(nums, k):
    result = 0
     
    count_map = {}
    for num in nums:
        count_map[num] = count_map.get(num,0) + 1
    for num in nums:
        low = num - k  
        if low in count_map.keys():
            result += count_map.get(low)
        
        # if high in count_map.keys():
        #     result += count_map.get(high)
            
    print(result)
    return result 
nums = [1,2,2,1]
k = 1
nums = [3,2,1,5,4]
k = 2
nums = [1,3]
k = 3
print(countKDifference(nums,k))