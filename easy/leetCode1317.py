#1317. Convert Integer to the Sum of Two No-Zero Integers
import math
def getNoZeroIntegers(n):
    result = []
    for i in range(1,int(math.sqrt(n))):
        
        firstNoZero = secondNoZero = False
        first,second = i, n - i 
        firstVal, seconVal = first,second
        print()
        while first:
            mode = first % 10
            if mode == 0:
                break
            else :
                first  = first// 10
        if first == 0:
            firstNoZero = True 
        while second:
            mode = second % 10
            if mode == 0:
                break
            else:
                second = second // 10
        if second == 0:
            secondNoZero = True
        print(firstVal,firstNoZero,seconVal, secondNoZero)
        if secondNoZero and firstNoZero:
            print(firstVal, seconVal)
            return [firstVal, seconVal]
 
getNoZeroIntegers(1057)