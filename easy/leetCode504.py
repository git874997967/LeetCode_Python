#504 base-7 
def convertToBase7(num):
    if num == 0:
        return "0"
    result , abs_num = "", abs(num)
    while abs_num > 0:
        result = str( abs_num % 7) + result 
        abs_num = abs_num // 7

    return result if num > 0 else "-" + result 

print(convertToBase7(98))

print(convertToBase7(101))


