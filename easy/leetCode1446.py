#1446. Consecutive Characters
def maxPower(s):
    mP,curLen  = 1,1 
    for index in range(1,len(s)):
        if s[index] == s[index -1]:
            curLen += 1
            mP = max(mP,curLen)
        else:
            curLen = 1
         
    print(mP)

maxPower("leetCode")

maxPower("abbcccddddeeeeedcba")

maxPower("triplepillooooow")

maxPower("hooraaaaaaaaaaay")

maxPower("tourist")

 