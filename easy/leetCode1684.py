#1684. Count the Number of Consistent Strings
def countConsistentStrings(allowed, words):
    result = len(words)
    for word in words:
        for char in word:
            if char not in allowed:
                result -= 1
                break
    return result