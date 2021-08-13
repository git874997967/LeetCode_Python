#709. To Lower Case
def toLowerCase(s):
    result = ""
    for char in s:
         if ord(char) >= 65 and ord(char) <= 90:
             newchar = chr(ord(char) + 32)
             result += newchar
         else:
             result += char
    return result  

print(toLowerCase('LOV^&ELY'))


def toLowerCase2(s):
    return "".join(chr(ord(c)+ 32) if (ord(c) >= 65 and ord(c)>= 90) else c for c in s)