#1118. Number of Days in a Month
def numberOfDays(year, month):
    daysMap = {}
    for i in range(1,13):
        if i in (1,3,5,7,8,10,12):
            daysMap[i] = 31
        elif i in (4,6,9,11):
            daysMap[i] = 30
        else:
            daysMap[i] = 28
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 and year % 3200 != 0) or year % 172800 ==0:
        if month == 2:
            return 29
    
    return daysMap[month]

print(numberOfDays(1656,12))

