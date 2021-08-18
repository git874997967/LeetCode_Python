# 830. Positions of Large Groups
def largeGroupPositions(s):
    res = []
    left, right = 0, 0 
    while right < len(s):
        while right < len(s) and s[right] == s[left]:
            right += 1
        if right - left >= 3:
            res.append([left,right - 1])
        left = right 
    print(res)
    return res

         
            
       
largeGroupPositions("abbxxxxzzy")

largeGroupPositions("abcdddeeeeaabbbcd")

largeGroupPositions("aba")