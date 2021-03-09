# 168. Excel Sheet Column Title
def convertToTitle(columnNumber):
    
    output = ''
    dict = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while columnNumber:
        reminder = columnNumber % 26
        output += dict[reminder]
        columnNumber = columnNumber // 26


    print(output[::-1])
    return output

test = 2147483647     # FXSHRXW
convertToTitle(test)
