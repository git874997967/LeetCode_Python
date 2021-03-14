# 41. First Missing Positive
def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(1,len(nums)):
        nums[nums[i] %n] += n # only add n can make the %n  still the same as num[i]  excellent 
    for i in range(1,len(nums)):
        if nums[i] == 0:
            return i
    return n 