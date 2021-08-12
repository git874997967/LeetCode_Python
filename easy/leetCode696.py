# 696. Count Binary Substrings (mid) 
def countBinarySubstrings(s):
    groups = [1]
    for i in range(1,len(s)):
        if s[i - 1] != s[i]:
            groups.append(1)
        else:
            groups[-1] += 1
    ans = 0 
    for i in range(1,len(groups)):
        ans += min(groups[i -1], groups[i])
    return ans 

def  countBinarySubstrings2(s):
    ans , prev, cur =  0, 0 , 1
    for i in range(1,len(s)):
        if s[i -1] != s[i]:
            ans += min(prev, cur)
            prev, cur = cur, 1
        else :
            cur += 1
    return ans + min(prev, cur)


def countBinarySubstring3(s):
    # prev ,cur represents the previou and current group of num  
    # s[i] != s[i-1] can split the 10 and 01 into diff groups
    ans, prev, cur = 0 , 0 , 1
    for i in range(1, len(s)):
        # we have the split and ans is the shorter length of two groups
        if s[i-1] != s[i]:
            ans += min(prev, cur)
            prev , cur = cur, 1 
        else:
            cur += 1
    return ans + min(cur, prev )
# a better understand the question:
# after split the 01 and 10  we group each char in a group  
# if they mixed the result is to find the min length for each cross 

def countBinarySubstring3(s):
    print(s.replace("01","0 1").replace("10", "1 0"))
    c = list(map(len, s.replace('10', '1 0').replace('01', '0 1').split()))
    res = 0
    for i in range(1, len(c)):
        res += min(c[i], c[i-1])
    print(res)
    return res


print(countBinarySubstring3("00110011"))
print(countBinarySubstring3("110001111000000"))

