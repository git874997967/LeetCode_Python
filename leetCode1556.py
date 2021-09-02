#1556. Thousand Separator
def thousandSeparator(n):
        if n < 1000:
            return str(n)
        result = str(n)
        arr , strLen = [], len(result)
        for i in range(strLen,2,-3):
            arr.insert(0,result[i-3:i])
            arr.insert(0,".")
        if i != 3:   
            arr.insert(0,result[0:i-3])
        print(arr)
        if arr[0] == '.':
            res = arr[1:]
            print(''.join(res))
        else:
            print(''.join(arr))
     
thousandSeparator(1000)
thousandSeparator(12345678)
thousandSeparator(123456789)
thousandSeparator(1234)
thousandSeparator(123456)
