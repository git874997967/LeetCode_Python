# 482. License Key Formatting
def licenseKeyFormatting( s, k):
    count ,result = 0, ""
    for i in  range(len(s) -1,-1,-1):
        if s[i] == "-":
            continue
        result += s[i]
        count += 1
        if count == k:
            result += '-'
            count = 0
    if len(result) == 0:
        return result
    if result[len(result) - 1] == "-":
        result = result[:len(result) - 1]
    return result[::-1].upper()



# char.join( array) will be a better way  
def licenseKeyFormatting2(s,k):
     # reverse  remove - and turn to upper
     licenseStr = s.replace("-", "").upper()[::-1]
     licenseArr = []
     for i in range(0,len(licenseStr), k): #  from 0 to len(licStr) each time move k digits
         licenseArr.append(licenseStr[i: i + k]) # cover k digits 
     if len(licenseArr) == 0:
         return ""
     return "-".join(licenseArr)[::-1]

print(licenseKeyFormatting2( "5F3Z-2e-9-w",   4))

print(licenseKeyFormatting2( "2-5g-3-J",  2))