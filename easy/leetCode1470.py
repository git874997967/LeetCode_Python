#1470. Shuffle the Array
def shuffle(nums, n):
    result = []
    for index in range(len(nums)/2):
        result.append(nums[index])
        result.append(nums[index+ n])
    return result