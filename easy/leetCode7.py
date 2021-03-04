# 7 reverse Integer
# take care the base case
def reverse(x):
    if x < 0:
        x = x * -1
        result = int(str(x)[::-1]) * - 1
    else:
        result = int(str(x)[::-1])
    # bound check 
    if (result < -2 ** 31) or (result > 2 ** 31 -1 ):
        return 0
    return result

