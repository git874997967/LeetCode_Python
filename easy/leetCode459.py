# 459. Repeated Substring Pattern

def repeatedSubstringPattern(s):
     
    result,length = False, len(s) 
    for i in range(1,length //2 + 1):
        if length % i == 0:
            if s[:i] * (len(s) // i) == s:
                return True
    return result

# lets say the repeat string A is (a + a ) 
# if s[1:](a` + a ) + s[: -1]( a + a `) contains A
# means (a` + a + a + a`) => (a` + A + a`) 

def repeatedSubstringPattern(s):
    return s in s[1:] + s[:-1]


string = "aa"
string1 = "abcdafabcdaf"
string2 = "aba"


print(repeatedSubstringPattern(string))
print(repeatedSubstringPattern(string1))

print(repeatedSubstringPattern(string2))