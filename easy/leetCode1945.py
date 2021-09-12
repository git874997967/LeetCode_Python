#1945. Sum of Digits of String After Convert
def getLucky(s, k):
    numArr=  ""
    for char in s:
        numArr += str(ord(char) - 96)

    while k > 0:
        result = 0
        for i in range(len(numArr)):
            result += int(numArr[i])
        numArr = result    
        k -= 1
    return int(numArr)

