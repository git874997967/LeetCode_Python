def countValidWords(sentence):
    str_list = sentence.split(' ')
     
    result = 0
     
    for str in str_list:
        is_digit = all_lower = one_hyphen = one_pun = False
        is_digit = any(char.isdigit() for char in str)
        if len(str) > 0 and str.lower() == str:
            all_lower = True 
        if str.count('-') == 0 or  \
        (str.index('-') == 1 and str.index('-') != len(str) - 1):
            one_hyphen = True 
        if str.count(',') + str.count('.') + str.count('!') == 1 and str[-1] in (',','.','!')  or \
            (str.count(',') + str.count('.') + str.count('!') == 0):
            one_pun = True 
        print(f"{str}: one_hyphen:{one_hyphen}, one_pun:{one_pun}, all_lower:{all_lower}")
        if one_hyphen and one_pun and all_lower and not is_digit:
            result += 1
    print(result)
    
countValidWords("!")
countValidWords(".")
countValidWords("-")
countValidWords("cat and  dog")




