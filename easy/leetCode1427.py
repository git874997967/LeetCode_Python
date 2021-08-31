#1427. Perform String Shifts
def stringShift(s, shift):
    newS = s + s 
    finalDir = 0
    for dir in shift:
        if dir[0] == 0:
            finalDir += dir[1]
        else:
            finalDir -= dir[1]
    finalDir = finalDir % len(s)
    print(newS[finalDir:finalDir + len(s)])

# "bca"
# "efgabcd"
# "yisxjwry"
s="abcdefg" 
shift = [[1,1],[1,1],[0,2],[1,3]]
stringShift(s,shift)

s="abc" 
shift = [[1,1],[0,2]]
stringShift(s,shift)

s = "yisxjwry"
shift = [[1,8],[1,4],[1,3],[1,6],[0,6],[1,4],[0,2],[0,1]]
stringShift(s,shift)