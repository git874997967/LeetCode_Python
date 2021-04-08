# 171. Excel Sheet Column Number
def titleToNumber(columnTitle):
    ans , index = 0,1
    for char in columnTitle[::-1]:
        ans += (ord(char) - 64) * 26 ** (index - 1)
        index += 1
    return ans
num = titleToNumber("ABC")
print(num)