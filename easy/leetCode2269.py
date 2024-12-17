def divisorSubstrings(num,k):
    str_num = str(num)
    result = 0
    for i in range(len(str_num) - k + 1):
        int_num = int(str_num[i:i+k])
        if int_num != 0 and num % int_num:
            result += 1
            
    print(result)    


divisorSubstrings(430043,2)
