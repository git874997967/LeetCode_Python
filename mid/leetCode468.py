 #468. Validate IP Address
def validIPAddress(IP):
    def validIPv4(IP):
       nums = IP.split(".")
       for num in nums:
          if  len(num) < 1 or len(num) > 3  or ( len(num) > 1 and num[0] == '0') or  not num.isdigit() or int(num)  > 255:
              return "Neither"
       return 'IPv4'
    def validIPv6(IP):
        nums = IP.split(":")
        validChar = list("0123456789abcedfABCDEF")
        for num in nums:
            if len(nums) == 0 or len(nums)> 5:
                return "Neither"
            else:
                for char in num:
                    if char not in validChar:
                        return "Neither"
        return "IPv6"
    if len(IP.split(".")) == 4:
        
        return validIPv4(IP)
    elif len(IP.split(":")) == 8:
     
        return validIPv6(IP)
    return "Neither"

 