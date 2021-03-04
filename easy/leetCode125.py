# 125. Valid Palindrome
# we need both numeric and alphabet
def isPalindrome(s):
    new_lower = filter(str.isalpha, s)
    lowerStr = ''.join(list(new_lower))
    new_lower = lowerStr.lower()
    print(new_lower)
    for i in range(len(new_lower)//2):
         
        print(new_lower[i], new_lower[-(i+1)])
        
string = "`Z3,njA3x x Ajn, Z`"

print(isPalindrome(string))
# two pointers python has the feature - index to iterate array from end of array
def isPalindrome2(self, s: str) -> bool:
    start , end = 0, len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
    return True
     