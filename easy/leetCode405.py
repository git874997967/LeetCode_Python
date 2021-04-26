# convert-a-number-to-hexadecimal
def toHex(self, num: int) -> str:
    if num == 0:
         return '0'
    bitMap = '0123456789abcdef'
    result = ''
    if num < 0 :
        num += 2 ** 32
    while num > 0:
         digit = num % 16
         num = (num - digit) // 16
         result += str(bitMap[digit])
    return result[::-1]


print(26 & (2>>4-1) )