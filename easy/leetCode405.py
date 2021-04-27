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

def toHex(num):
    bitMap = '0123456789acdef'
    if num == 0:
        return '0'
    result = ''
    if num < 0:
        num += 2 ** 32 
    while num > 0 :
        reminder = num % 16
        num = (num - reminder ) // 16
        result += str(bitMap[reminder])
    # reverse the result 
    return result[::-1]