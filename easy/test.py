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

def townJudge(n,trust):
    outArr,inArr,candidate = [0] *(n + 1),[0] * (n + 1), 0
    if n - 1> len(trust) : 
        return -1
    for i,j in trust:
        outArr[i] += 1
        inArr[j] += 1
    for i in range(1,n + 1):
        if inArr[i] == n -1 and outArr[i] == 0:
            return i
    return -1

def townJudge2(n, trust):
    if len(trust) < n -1:
        return -1 
    turstScore = [0] * (n-1)
    candidate = 0
    for i , j in trust:
        if candidate == i:
            return - 1
        turstScore[i] -= 1
        if turstScore[j] >= 0:
            turstScore[j] += 1
            if turstScore[j] == n - 1:
                return j
    return candidate or -1

selfDividingNumbers(1,22)


selfDividingNumbers(47,85)

#
