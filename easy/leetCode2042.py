def areNumbersAscending(s):
    str_list = s.split(' ') 
    max_num = 0
    for s_num in str_list:
        if s_num.isnumeric():
            num = int(s_num)
            if num > max_num:
                max_num = num 
            else:
                return False
    return True


s = "a puppy has 2 eyes 4 legs"
s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(areNumbersAscending(s))