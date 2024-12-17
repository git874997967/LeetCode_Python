def digitSum(s,k):
    result = s 
    while len(result) > k:
        tmp_list = []
        for i in range(0,len(result),k):
            tmp_list.append(result[i:i+k])
        num_list = []
        for tmp in tmp_list:
            # 111 -> 3
            new_tmp = sum(int(char) for char in tmp)
            num_list.append(str(new_tmp)) #['3','4','6','5']
        result = ''.join(num_list)

    print(str(result))
    
digitSum('11111222223',3)

digitSum("00000000",3)