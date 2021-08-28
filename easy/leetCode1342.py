#1342. Number of Steps to Reduce a Number to Zero
import math
def numberOfSteps( num):
    result = 0
    if int(math.log2(num)) - math.log2(num) == 0:
         
        return int(math.log2(num) + 1)
    while num :
        if num % 2 == 1:
            num -= 1
        elif int(math.log2(num)) - math.log2(num) == 0:
           
            return int(result + math.log2(num) + 1)
        else:
            num = num //2
        result += 1
     
    return int(result)

 
numberOfSteps(32)
numberOfSteps(8)
numberOfSteps(14)
numberOfSteps(13)
