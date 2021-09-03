#1636. Sort Array by Increasing Frequency
def frequencySort(nums):
    freqMap ,result = {}, []
    for num in nums:
        freqMap[num] = freqMap.get(num,0) + 1
    orderMap = sorted(freqMap.items(),key = lambda x:(x[1],-x[0]) )
    for k,v in orderMap:
        result += [k] * v
    print(result)

frequencySort([1,1,2,2,2,3])
frequencySort([1,1,2,2,2,3]
[2,3,1,3,2]
[-1,1,-6,4,5,-6,1,4,1])