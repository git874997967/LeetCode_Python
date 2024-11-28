def scoreOfString(s):
    char_array = [ord(c) for c in s]
    result = sum(abs(char_array[i] - char_array[i-1]) for i in range(1,len(char_array)))
    print(result)
    
scoreOfString('zaz')