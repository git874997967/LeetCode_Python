#1323. Maximum 69 Number
def maximum69Number (num):
    strNum ,result= str(num), ""
    find = False 
    for i in range(0,len(strNum)):
        if not find and strNum[i] == '6':
          result += '9'
          find = True
        else:
            result += strNum[i]
    return int(result)

print(maximum69Number(69))


print(maximum69Number(69))
print(maximum69Number(9669))

