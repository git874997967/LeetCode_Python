# 67. Add Binary
# fill the dummy with the max length  with zero and then calculate one by one until the first index  Used in add one 
#  Use zfill method and then calculation
def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    result = []
    flag = 0
    maxLength = max(len(a), len(b))
    a , b = a.zfill(maxLength), b.zfill(maxLength)
    for i in range( maxLength -1, -1, -1):
         value = int(a[i]) + int(b[i]) + flag
         if value == 3 :
            flag = 1 
            result .append('1')
        elif value == 2:
            flag = 1
            result.append('0')
        elif value == 1:
            flag = 0
            result.append('1')
        else:
            flag = 0
            result.append('0')
        
    result.reverse()
    return ''.join(result)
    