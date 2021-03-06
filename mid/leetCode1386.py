# 1386. Cinema Seat Allocation
def maxNumberOfFamilies(n, reservedSeats):
    result = n * 2 
    reservedSeats.sort(key = lambda x,y: x[0] -y[0])
    row = 0 
    while row < reservedSeats.length:
        prev = reservedSeats[row][0]
        leftOccupied = midOccupied = rightOccupied = False 
        while row < reservedSeats.length and reservedSeats[row][0] == prev:
            if reservedSeats[row][i] >=2 and reservedSeats[row][i] <= 5:
                leftOccupied = True
            if reservedSeats[row][i] >=4 and reservedSeats[row][i] <= 7:
                midOccupied = True
            if reservedSeats[row][o] >=6 and reservedSeatsp[row][i] <= 9:
                rightOccupied = True
            row += 1
        if midOccupied:
            if leftOccupied:
                result -= 1
            if rightOccupied:
                result -= 1
        if leftOccupied or rightOccupied :
            result -= 1
    return result 

# better solution 

def  maxNumberOfFamilies2(n,reversedSeats):
    rowSeats = {}
    for seats in reversedSeats:
        if seats[0] not in rowSeats:
            rowSeats[seat[0]] = [0] * 11   # 1...10
        rowSeats[seats[0]][seat[1]] += 1
    result = 0
    for rowKey in rowSeats.keys():
        rows = rowSeats[rowKey]
        found = False # this need inside the loop and always be false when iterate a new row line
        if rows[2] == 0 and rows[3] == 0 and rows[4] == 0 and rows[5] == 0:
            found = True
            result += 1
        if rows[6] == 0 and rows[7] == 0 and rows[8] == 0 and rows[9] == 0:
            found = True
            result += 1
        if not found:
            if rows[4] == 0 and rows[5] == 0 and rows[6] == 0 and rows[7] == 0:
                result += 1
    result += (n - len(rowSeats)) * 2 # empty row will not be shown so we can put two families
    return result        
