#1876. Substrings of Size Three with Distinct Characters
def countGoodSubstrings(s):
    result = 0 
    for i in range(len(s) - 2):
        subStr = s[i:i + 3]
        print(subStr)
        if len(set(subStr)) == 3:
            result += 1
    return result


countGoodSubstrings("aababcabc")