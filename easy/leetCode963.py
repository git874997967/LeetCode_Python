#961. N-Repeated Element in Size 2N Array
def repeatedNTimes( nums):
    numSet = set()
    for n in nums:
        if n in numSet:
            return n 
        else:
            numSet.add(n)


def repeatedNTimes2(nums):
#every 4 sliding windows must contain the  repeated numbers
    for i in range(0,4):
        for j in range(len(nums)-j):
            if nums[j] == nums[j + i]:
                return nums[j]
