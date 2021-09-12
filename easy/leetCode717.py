#717. 1-bit and 2-bit Characters
# We have two special characters:
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
def isOneBitCharacter(bits):
     oneSec = True 
     i  = 0 
     while i < len(bits):
         if bits[i] == 1:
             i += 2
             oneSec = True
         else:
             i += 1
             oneSec = False
     return not oneSec

def isOneBitCharacter(bits):
    i = 0
    while i < len(bits) - 1:
        i += 2 if bits[i] == 1 else 1
    return i != len(bits)

print(isOneBitCharacter([0,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0]))

print(isOneBitCharacter([0,0,0]))