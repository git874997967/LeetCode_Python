# 9. Palindrome Number
# solution 1  convert to string
def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# solution 2  without string transfer
def isPalindrome(x):
    if x < 0 :
        return False
    newNum = 0
    oldNum = x
    while x > 0 :
        newNum = newNum * 10 + x % 10
        x = x // 10  #  pill the last digit and remain others
    return newNum == oldNum