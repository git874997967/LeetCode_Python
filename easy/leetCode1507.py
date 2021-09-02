#1507. Reformat Date
def reformatDate(date):
    monthMap  ={"Jan": "01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
    dateStr = date.split(" ")
    date = ""
    for char in dateStr[0]:
        if char.isdigit():
            date += char 
    if int(date) < 10:
         date = '0' + date 
    print(dateStr[2] + '-' + monthMap.get(dateStr[1]) + '-' + date)
    return dateStr[2] + '-' + monthMap.get(dateStr[1]) + '-' + date

reformatDate("20th Oct 2052") 
reformatDate("6th Jun 1933") 
reformatDate("26th May 1960") 
 