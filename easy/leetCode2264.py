def largestGoodInteger(num):
    result = 0
    for i in range(0,len(num)-2):
        tmp_str = num[i:i+3]
        if tmp_str[0] == tmp_str[1] == tmp_str[2]:
            result = max(result, int(tmp_str))
    print(str(result) if result != 0 else "")
    return str(result) if result != 0 else ""

largestGoodInteger('6777133339')
largestGoodInteger('42352338')