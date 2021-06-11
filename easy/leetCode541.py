# 541. Reverse String II
def reverseStr(s,k):
    result = list(s)
    for i in range(0, len(s),2 * k):
        result[i:i+k] = result[i:i+k][::-1]
    return ''.join(result)


def  reverseStr1(s,k):
    i,length,result = 0,len(s),""
    while i < length:
        if k <= abs(length - i) < 2 * k:
            final = final + s[i:i+ k][::-1] + s[i+k:length]
        elif abs(length - i) < k:
            final = final + s[i:length][::-1]
        else:
            final = final + s[i:i+k][::-1] + s[i+k:i+ 2* k]
        i = i + 2  * k
    return result 

print(reverseStr("abcdefg",2))


print(reverseStr("abcd",2))

         

