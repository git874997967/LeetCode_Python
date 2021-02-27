# 66 plus one 
def plusOne(digits):
    flag = 1
    for i in range(len(digits)-1,0,-1):
       # print(digits[i])
    #    result = digits[i] + flag 
    #    if result == 10:
    #        flag = 1 
    #        digits[i] = 0
    #    else:
    #         flag = 0
    #         digits[i] = result
        if digits[i] + flag == 10:
            flag = 1
            digits[i] = 0
        else:
            digits[i] += flag
            flag = 0
    if digits[0] + flag == 10:
        digits[0] = 0
        return [1]+ digits
    else:
        digits[0] += flag
    return digits

array = [2,9,3,2,4]
result = plusOne(array)
print( result)
def  plusOne2(digits):
    flag = 1 
    for i in range(len(digits)-1, -1, 0):
        if digits[i] + flag == 10:
            flag = 1
            digits[i] = 0
        else:
            digits[i] += flag
            flag = 0 
    if digits[0] + flag != 10:
        digits[0] += flag
        return digits
    else:
        digits[0] = 0
        return [1] + digits