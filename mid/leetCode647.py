#647. Palindromic Substrings
def countSubstrings(s):
    ans = 0
    def expand(s,left,right):
        ans = 0
        while left >= 0 and right < len(s)  :
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
            ans += 1
        return ans
    for i in range(len(s)):
        ans += expand(s,i,i)
        ans += expand(s,i,i + 1)
    return ans


countSubstrings("babab")
countSubstrings("aaa")
countSubstrings("babfdfgdddeedwsdwwx")