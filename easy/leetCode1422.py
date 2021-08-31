#1422. Maximum Score After Splitting a String
def maxScore(s):
    maxScore = float('-inf')
    for i in range(1,len(s)):
        left,right = s[0:i], s[i:len(s)]
        maxScore = max(maxScore, left.count('0') + right.count('1'))

    print(maxScore)
    return maxScore

maxScore("011101")