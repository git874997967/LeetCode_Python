#1796. Second Largest Digit in a String
def secondHighest(s):
    charSet = set()
    for char in s :
        if char.isdigit():
            charSet.add(int(char))
    charSet.sort(reverse = True )
    return -1 if len(charSet) <2 else charSet[1]
