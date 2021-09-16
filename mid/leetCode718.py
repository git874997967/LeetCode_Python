#718. Maximum Length of Repeated Subarray
def findLength(A, B):
    def maxLength(addA,addB,length):
        result = k = 0
        for i in range(length):
            if A[addA + i] == B[addB + i]:
                 k += 1
                 result = max(result,k)
            else:
                k = 0 
        return result

    m , n = len(A),len(B)
    
    for i in range(n):
        length = min(m,n-i)
        result = max(result,maxLength(i,0,length))
    
    for i in range(m):
        length = min(n,m - i)
        result = max(result, maxLength(0,i,length))
    
    return result 


def findLength2(A,B):
    m, n = len(A), len(B)
    dp = [[0] *(m +1) for _ in range(n + 1)]
    result = 0
    for i in range(n-1, -1,-1):
        for j in range(m - 1, -1,-1):
            dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else  0 
            result = max(result,dp[i][j])
    return result    


findLength([1,2,3,2,1],[3,2,1,4,7])

findLength([0,0,0,0,0],[0,0,0,0,0])

findLength([0,0,0,0,1] ,[1,0,0,0,0])

findLength([0,1,1,1,1],[1,0,1,0,1])