# 88. Merge Sorted Array
# reverse : confirm the last element  and then move forward
def merge( n1 , n2, m, n):
    while m > 0 and n > 0:
        # confirm the last number first
        if n1[m -1 ] > n2[n - 1 ]:
            n1[m + n - 1 ] = n1[m - 1]
            m -= 1
        else:
            n1[ m + n - 1] = n2[n - 1]
            n -= 1
        n1[ :n] = n2[ :n]


        
