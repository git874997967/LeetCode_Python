#1137. N-th Tribonacci Number
def tribonacci(n):
    result = [0,1,1,2]
    for i in range(4,n+1):
        result.append(result[i-2] + result[i-1] + result[i-3])
     
    return result[n]

tribonacci(4)
tribonacci(25)


    