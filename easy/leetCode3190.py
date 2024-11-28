def minimumOperations(nums):
     return sum(1 if num %3 != 0 else 0 for num in nums)