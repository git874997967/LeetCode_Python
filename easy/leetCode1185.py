#1185. Day of the Week
def dayOfTheWeek(day, month, year):
    dates = ['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
    monthMap = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
    days = 0
    days = day + monthMap[month] - 1
    
        # end year is leap and month big than 2
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 and year % 3200 != 0) or year % 172800 ==0:
        if month > 2:
            days += 1
    # count all dates in the year in the middle [1971,year)
    for i in range(1971,year):
        if (i % 4 == 0 and i % 100 != 0 ) or (i % 400 == 0 and i % 3200 != 0) or i % 172800 ==0:
            days += 366 
        else:
            days += 365

    return dates[days%7]
    
print(dayOfTheWeek(5,8,2000))