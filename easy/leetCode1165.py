#1165. Single-Row Keyboard
def calculateTime( keyboard, word):
    charArr = [i for i in keyboard]
    
    result = 0
    start = 0
    for char in word:
        print(charArr.index(char),start)
        result += abs(charArr.index(char) - start)
        start = charArr.index(char)
    return result
keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
print(calculateTime(keyboard, word))

keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(calculateTime(keyboard, word))