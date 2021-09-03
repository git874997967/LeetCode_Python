#1694. Reformat Phone Number
def reformatNumber(number):
    result = []
    digArr = number.replace(' ','').replace('-','')
     
    if len(digArr) <= 3:
        return digArr
    for i in range(0,len(digArr) -2,3):
        
        result += digArr[i:i+3]
        result.append("-")

    if len(digArr) - i - 3 == 0:
        result[-1] = ""
    elif len(digArr) - i - 3 ==2:
       result.append(digArr[-2:])
    elif len(digArr) - i - 3 == 1:
         
        newEnd = result[-4:-1]
        newEnd.append(digArr[-1])
         
        result = result[:-4]
        result += newEnd[0:2] + ["-"] + newEnd[2:]
        
    
    print(''.join(result))
reformatNumber("1-23-45 6")
reformatNumber("123 4-567")
reformatNumber("123 4-5678")
reformatNumber("1234")
reformatNumber( "--17-5 229 35-39475 ")