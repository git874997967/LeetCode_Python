# 415. Add Strings
def addStrings( num1, num2):
     if num1 == '0' :
         return num2
     elif num2 == '0':
         return num1 
     flag,result = 0, ''
     num1 ,num2 = num1[::-1], num2[::-1]
     pNum1, pNum2 = 0,0
     while pNum1 < len(num1) and pNum2 < len(num2):
        value = int(num1[pNum1]) + int(num2[pNum2])  + flag 
        if value >= 10:
            # result.append(str(value % 10))
            result += str(value % 10)
            flag = 1
        else:
            result += str(value % 10)
            flag = 0
        pNum1 += 1
        pNum2 += 1
     while pNum1 < len(num1):
         value = int(num1[pNum1]) + flag
         if value >= 10:
             result += str(value % 10)
             flag = 1
         else:
             result += str(value % 10)
             flag = 0
         pNum1 += 1
     while pNum2 < len(num2):
         value = int(num2[pNum2]) + flag
         if value >= 10:
             result += str(value % 10)
             flag = 1
         else:
             result += str(value % 10)
             flag = 0
         pNum2 += 1
     if flag == 1:
        result += '1'
     return int(result[::-1])
print(addStrings('1','99'))

print(addStrings("11",'123'))

print(addStrings('456','77'))
  
print(addStrings('0','0'))
           

