#989. Add to Array-Form of Integer
def addToArrayForm2( num, k):
    if k == 0 :
        return num
    result = 0
    for i in range(len(num) - 1,-1,-1):
        result += num[i] * 10 **(len(num) - 1 - i)
    result += k
    arr = []
     
    while result  > 0:
        bit = result % 10  
        arr.append(int(bit))
        result -= bit 
        result = result / 10
    arr = arr[::-1]
    print(arr)
 
def addToArrayForm3( num, k):
    strNum = ""
    divmod
    for i in num:
        strNum += str(i)
    result = list(str(int(strNum) + k))
    return [int(i) for i in result]

#divmod

def addToArrayForm(num,k):
    for i in range(len(num) - 1,-1,-1):
        k,num[i] = divmod(num[i] + k, 10)
        print(k,num[i])
    return [int(i) for i in str(k)] + num if k else num 
     
     




addToArrayForm([1,2,0,0],34)
#1234
addToArrayForm([2,7,4],181)
# 455
addToArrayForm([2,1,5],806)

addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1)