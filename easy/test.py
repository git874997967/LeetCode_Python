# test
def  valid(s):
    start, end = 0, len(s) - 1
    while start < end:
        # str1 skip the end and str2 skip then start
        if s[start] != s[end]:
            str1 , str2 = s[start:end],s[start + 1: end + 1]
            return  str1 == str1[::-1] or str2 == str2[::-1]
        start += 1
        end -= 1
    return True

def  reverseStr(s, k):
    result = list(s)
    for i in range(0, len(s), 2 * k):
        result[i: i + k] = result[i:i+ k][::-1]
    return ''.join(result)

def reverseStr2(s, k):
    i, length, final = 0, len(s), ""
    for i in range(0,length, 2 *k):
        if k < abs(length - i) < 2 * k :
            final += s[i:i + k ][::-1] + s[i + k:length]
        elif abs(length - i) < k:
            final += s[i: length][::-1]
        else:
            final += s[i:i + k][::-1] + s[i+k:i + 2 * k]
       
    return final 

def selfDividingNumbers( left, right):
    result = []
    for i in range(left,right + 1):
        num , diviable = i, True 
        while num > 0:
            print(num)
            digit = num % 10
            if digit == 0 or i % digit != 0:
                diviable = False
                break
            num = num // 10
        if diviable:
            result.append(i)

            
    return result


selfDividingNumbers(1,22)


selfDividingNumbers(47,85)

#
