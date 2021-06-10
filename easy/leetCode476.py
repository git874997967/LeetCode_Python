# 476. Number Complement
def findComplement( num):
     todo, bit = num, 1
     while todo :
         num = num ^ bit 
         bit = bit << 1
         todo = todo >> 1
     return num

print(findComplement(7))


print(findComplement(5))
