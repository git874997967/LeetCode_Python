#1389. Create Target Array in the Given Order
def createTargetArray(nums, index):
    result = [nums[0]]
    if len(nums) == 1:
        return  result * len(index)

    for ind in range(1,len(index)):
        if index[ind] < ind:
            print("call insert")
            result.insert(index[ind],nums[ind])
        else:
            result.append(nums[ind])
        print(result)
    
    return result

createTargetArray([1],[0])
createTargetArray([1,2,3,4,0],[0,1,2,3,0])
