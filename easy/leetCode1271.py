#1271. Hexspeak
def toHexspeak(num):
    result ,hexStr = "", str(hex(int(num)))[2:]
    print(hexStr)
    for i in hexStr:
        if i == '1':
            result += 'I'
        elif i == '0':
            result += 'O'
        elif i in ['2','3','4','5','6','7','8','9']:
            return "ERROR"
        else:
            result += chr(ord(i) - 32)
    
    return result

print(toHexspeak(257))
print(toHexspeak(747823223228))
print(toHexspeak(3))