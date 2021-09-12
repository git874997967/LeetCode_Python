#1893. Check if All the Integers in a Range Are Covered
def isCovered(ranges, left, right):
     coverArr = [0] * 51
     for index in ranges:
         for i in range(index[0],index[1]+ 1):
             coverArr[i] += 1

     for index in range(left,right + 1):
         if coverArr[index] == 0:
           
             return False
     return True
    