# 910. Smallest Range II
# in a nutshell we need two pointers with two speeds  
# behind with + 2K speed  and  previous with +0 speed
# the value bound should between A0  to A-1 and the Ai in between should bounce with Ai + 2K
def smallestRangeII(self, A, K):
    A.sort()
    result = A[-1] - A[0]
    for i in range(len(A) - 1):
        mx = max(A[-1], A[i] + 2 * K)
        mn = min(A[i + 1], A[0] + 2 * K)
        result = min(result, mx - mn)
    return result
 
