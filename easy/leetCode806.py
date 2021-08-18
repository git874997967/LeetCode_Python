# 806. Number of Lines To Write String
def numberOfLines(widths, s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    charArr = [char for char in chars]
    charMap = dict(zip(charArr,widths))
    line , length = 0 , 0
    if len(s) == 1:
        return [0,charMap[s[0]]]

    for i in range(0, len(s) -1):
        length += charMap[s[i]]
         
        if length <= 100 and length+ charMap[s[i+1]] > 100:
            print("new line")
            line += 1
            length = 0

    line += 1
    length += charMap[s[-1]]

    return [line,length]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
print(numberOfLines(widths,s))
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaa"
print(numberOfLines(widths,s))



def numberOfLines2(widths,s):
    line,width = 1,0
    for c in s:
        w = widths[ord(c) - ord('a')] 
        width += w
        if width > 100:
             line += 1
             width = w 
    return [line,width]