# 202. Happy Number
def isHappy(n):
    happyCandidate = 0
    numSet = set()
    while n:
        while n:
            happyCandidate += (n % 10) ** 2
            n = n // 10
        if happyCandidate == 1:
            return True 
        if happyCandidate in numSet:
            return False
        numSet.add(happyCandidate)
        print(happyCandidate)
        n = happyCandidate
        happyCandidate = 0
print(isHappy(2))