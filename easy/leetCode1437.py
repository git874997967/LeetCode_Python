#1437. Check If All 1's Are at Least Length K Places Away
def kLengthApart(nums, k):
    result = True 
    curPos = [-1]
    for i in range(len(nums)):
        if nums[i] == 1 and curPos[0] == -1:
            curPos[0] = i
        elif nums[i] == 1 and i - curPos[0] >  k:
            curPos[0] = i
        elif nums[i] == 1 and i - curPos[0] <= k:
            return False
     
    return result

nums = [1,0,0,1,0,1]
k = 2

print(kLengthApart(nums,k))