# 163. Missing Ranges
# two pointers
def findMissingRanges(nums, lower, upper):
    result = []
    prev = lower -1 
    def  formatRange(num1, num2):
        if num1 == num2:
            return str(num1)
        return str(num1) + '->' + str(num2)
    for i in range( len(nums) + 1):
        cur = nums[i] if i < len(nums) else upper + 1
        if prev + 1 <= cur - 1:
            result.append(formatRange(prev + 1, cur - 1))
        # cur = prev move back  not forward
        prev = cur     
    return result
print(findMissingRanges([1,3,5,7,9],0,100))