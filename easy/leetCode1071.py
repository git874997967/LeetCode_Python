#1071. Greatest Common Divisor of Strings
def gcdOfStrings(str1, str2):
    if len(str1) > len(str2):
        str1,str2 = str2,str1
    for maxLength in range(len(str1),0,-1):
         
        if len(str1) % maxLength != 0 or len(str2) % maxLength != 0:
            continue
        else:
           time1 = len(str1) // maxLength
           time2 = len(str2) // maxLength
           if str1[0:maxLength] * time1 == str1 and str1[0:maxLength] * time2 == str2:
               return True
           
    return ""
                
        

gcdOfStrings("ABCDABCD","ABCD")
gcdOfStrings("LEET","CODE")

gcdOfStrings("ABABAB","AB")

gcdOfStrings("AAAAAAA","AAA")