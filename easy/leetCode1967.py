#1967. Number of Strings That Appear as Substrings in Word
def numOfStrings(patterns, word):
    result = 0
    for pattern in patterns:
        if pattern in word:
            result += 1
    return result