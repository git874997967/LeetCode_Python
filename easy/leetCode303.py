# 303. Range Sum Query - Immutable
class NumArray(object):
     
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [0]
        for num in nums:
            self.sum.append(self.sum[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sum[right + 1] - self.sum[left]       


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)