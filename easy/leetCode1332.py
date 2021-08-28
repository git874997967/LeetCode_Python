#1332. Remove Palindromic Subsequences
def removePalindromeSub(s):
    if s == s[::-1]:
        return 1
    return 2



    
print(removePalindromeSub("abb"))