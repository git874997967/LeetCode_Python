# 551. Student Attendance Record I
def checkRecord( s):
   absentCount, result = 0, True
   for status in s:
       if status == 'A':
           absentCount += 1
   return True if absentCount < 2 and "LLL" not in s else False


print(checkRecord("PPPALLL"))