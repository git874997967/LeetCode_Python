# 246. Strobogrammatic Number
def isStrobogrammatic(num):
    if len(num) == 1:
        return True if num == '1' or num == '0' else False
    else:
        start , end = 0, len(num) - 1
        while start <= end:
            
            if num[start] == '0' and num[end] == '0':
                 
                start += 1
                end -= 1
            elif num[start] == '8' and num[end] == '8':
                
                start += 1
                end -= 1
            elif (num[start] == '6' and num[end] == '9'):
                
                start += 1
                end -= 1
            elif  (num[start] == '9' and num[end] == '6'):
                 start += 1
                 end -= 1
            elif num[start] == '1' and num[end] == '1':
               
                start += 1
                end -= 1
            else:
               
                return False 
    return True 
 
print(isStrobogrammatic("659"))

 