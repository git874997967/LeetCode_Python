#253. Meeting Rooms II
def minMeetingRooms(Intervals):
    if not Intervals:
        return 0
    roomNum = 1
    Intervals.sort(key = lambda x:x[0])
    first = Intervals[0]
    for i in range(1,len(Intervals)):
        if first[1] > Intervals[i][0]: # have to use a new room
            roomNum += 1
            first = Intervals[i]
        else:
            first[1] = Intervals[i][1]
    return roomNum