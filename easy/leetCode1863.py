#1863. Sum of All Subset XOR Totals
def subsetXORSum(nums):
    N = 2 * len(nums)
    result = 0
    for i in range(2 ** N):
        xorResult = []
        
        for j in range(len(nums)):
            if (i>>j) %2 :
                xorResult.append(nums[j])
        
        print(xorResult)
        if len(xorResult) == len(nums) :
            break

def subsetXORSum1(nums):
        res=0
        for i in nums:
            res=res|i
        
        return res*(2**(len(nums)-1))
subsetXORSum([1,2,3]) 