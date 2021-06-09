# 461. Hamming Distance
def hammingDistance(x, y):
    return bin( x^ y).count('1')