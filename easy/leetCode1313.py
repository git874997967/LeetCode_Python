#1313. Decompress Run-Length Encoded List
def decompressRLElist(nums):
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
    result = []
    for index in range(1,len(nums)+1,2):
        print(index)
        result += nums[index-1] * [nums[index]]
    print(result)


decompressRLElist([1,2,3,4])

decompressRLElist([1,1,2,4])