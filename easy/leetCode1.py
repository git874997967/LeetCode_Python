#  1 two Sum
# use dict container  
# dict[key] => value
def twoSum(nums, target):
    dict = {}
    # use i, num to get both value and index from enumerate  obj
    for i , num in enumerate(nums):
        diff = target - num
        if(diff in dict) and (dict[diff] != i):
            # list(()) will return a array
            # return list((dict[num], i ))
            return [dict[num],i]
        dict[num]  = i
 