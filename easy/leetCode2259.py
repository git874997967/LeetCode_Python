def removeDigit(number,digit):
    result = 0
    for i ,num in enumerate(number):
        if num == digit:
            print(num,digit)
            new_char = number[:i] + number[i+1:]
            print(new_char)
            result = max(result, int(new_char))
            
    #print(result)
    
    
removeDigit('123','3')
removeDigit('1231','1')
removeDigit('551','5')