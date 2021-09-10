#1880. Check if Word Equals Summation of Two Words
def isSumEqual(firstWord, secondWord, targetWord):
    firstVal , secondVal , targetVal = 0 , 0 , 0 
    for char in firstWord:
        firstVal += ord(char) - 97
        firstVal *= 10
    firstVal //= 10
    for char in secondWord:
        secondVal += ord(char) - 97
        secondVal *= 10
    secondVal //= 10
    for char in targetWord:
        targetVal += ord(char) - 97
        targetVal *= 10
    targetVal //= 10

    return targetVal - firstVal == secondVal
    