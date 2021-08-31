#1365. How Many Numbers Are Smaller Than the Current Number
def smallerNumbersThanCurrent(nums):
    sortNum = sorted(nums)
    result , sortMap = [], {}
    for i,num in enumerate(sortNum):
        if num not in sortMap.keys():
            sortMap[num] = i
    print(sortMap)
    for num in nums:
        result.append(sortMap.get(num))
    print(result)

smallerNumbersThanCurrent([8,1,2,2,3])


smallerNumbersThanCurrent([6,5,4,8])