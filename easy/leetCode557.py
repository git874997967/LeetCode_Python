# 557. Reverse Words in a String III
def reverseWords(S):
    strArr, result = S.split(" "),""
    for str in strArr:
        str = str[::-1]
        result += str 
        result += " "
    return result

def reverseWords2(s):
    s = s.split(" ")
    for i, word in enumerate(s):
        s[i] = word[::-1]
    return " ".join(s)    

print(reverseWords("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"

print(reverseWords("God Ding"))  # "doG gniD"