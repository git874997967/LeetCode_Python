#1417. Reformat The String
def reformat(s):
    charArr = []
    digitArr = []
    result = ""
    for char in s:
        if char.isalpha():
            charArr.append(char)
        else:
            digitArr.append(char)
    if   abs(len(digitArr) - len(charArr)) > 1:
        return result
    elif len(digitArr) == 1 and len(charArr) == 0:
        return digitArr[0] 
    elif len(charArr) == 1 and len(digitArr) == 0:
        return charArr[0]

    else:
       if len(digitArr) > len(charArr):
           for i in range(len(charArr)):
               result += digitArr[i] + charArr[i]
                
           result += digitArr[i+1]
       elif len(charArr) > len(digitArr):
           for i in range(len(digitArr)):
               result += charArr[i] + digitArr[i]
                
           result += charArr[i+1]
       else:
            for i in range(len(digitArr)):
               result += charArr[i] + digitArr[i]

    return result

print(reformat("covid2019"))
print(reformat("012abc"))
print(reformat('j'))
print(reformat('1'))