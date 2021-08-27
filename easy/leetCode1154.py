#1154. Day of the Year
def dayOfYear(date):
    dateArr =date.split("-")
    year, month, day, result = int(dateArr[0]), int(dateArr[1]), int(dateArr[2]),0
    dayMap = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 and year % 3200 != 0) or year % 172800 ==0:
        if month >= 3:
            result = 1  
    return dayMap[month] +result + day

     