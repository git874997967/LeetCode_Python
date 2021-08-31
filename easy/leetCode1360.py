#1360. Number of Days Between Two Dates
def daysBetweenDates(date1, date2):
    return abs(self.days(date2) - self.days(date1))


def days(self,date):
    monthMap = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
    days = 0
    dateStr = date.split("-")
    year,month,day = int(dateStr[0]), int(dateStr[1]),int(dateStr[2])
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 and year % 3200 != 0) or year % 172800 ==0:
        if month > 2:
            days += 1
    for i in range(1971,year):
        if (i % 4 == 0 and i % 100 != 0 ) or (i % 400 == 0 and i % 3200 != 0) or i % 172800 ==0:
            days += 366 
        else:
            days += 365

    return day + days + monthMap[month]