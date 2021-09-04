#1844. Replace All Digits with Characters
def replaceDigits(s):
    result = ""
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i]
        else:
            result += chr(ord(s[i-1])+ int(s[i]))
    print(result)

    