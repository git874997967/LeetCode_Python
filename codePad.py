def removeDup(nums,target):
    i = 0
    for j in range(len(nums)):
        if nums[j] == target:
            continue
        else:
            nums[i] = nums[j]
            i += 1
    print(nums[:i])
    return nums[:i]

removeDup([0,1,2,2,3,0,4,2],2)