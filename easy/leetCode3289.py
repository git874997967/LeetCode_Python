def getSneakyNumbers(nums):
    single_num = set()
    result = []
    for num in nums:
        if num not in single_num:
            single_num.add(num)
        else:
            result.append(num)
            
    print(result)
    
getSneakyNumbers([0,3,2,1,3,2])
getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2])