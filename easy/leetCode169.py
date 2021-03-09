# 169. Majority Element
# vote algo   the major vote for one and all others vote for -1
def majorityElement( nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            #  use the num as the candidate 
            candidate = num
        count += (1 if candidate == num else - 1)
    print(candidate)
    return candidate
arr = [2,2,1,1,1,2,2,2]
majorityElement(arr)