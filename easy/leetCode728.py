# 728. Self Dividing Numbers
def selfDividingNumbers(left, right):
    result = []
    for num in range(left,right + 1):
        strNum = str(num)
        length = len(strNum)
        for digit in  range(len(strNum)):
            if strNum[digit] != '0' and num % int(strNum[digit]) == 0:
                length -= 1
        if length == 0:
            result.append(num) 
    return result 

def selfDividingNumbers2(left,right):
    result = []
    for i in range( left, right + 1):
        num , diviable = i, True
        while num > 0:
            digit = num % 10
             
            if digit == 0 or num % digit != 0:
                diviable = False
                break
            num = num // 10
        if diviable:
            result.append(i)
    return result 




print(selfDividingNumbers2(1,15))