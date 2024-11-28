def convertDateToBinary(date):
    date_list, date_str = date.split('-'),  []
    for d_10 in date_list:
        if d_10 == '01':
            date_str.append('1')
        else:
            
            date_str.append(bin(int(d_10))[2:])
    
    print('-'.join(date_str))
    

convertDateToBinary('1991-07-01') 