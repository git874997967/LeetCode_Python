#1374. Generate a String With Characters That Have Odd Counts
def generateTheString( n):
    if n % 2 == 1:
        return 'a' * n
    return (n-1) * 'a' + 'b' 


    return result


generateTheString(2)


generateTheString(4)


generateTheString(6)


generateTheString(8)