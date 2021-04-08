def get_free_time(cal1,cal2,duration,time):
     ans = []
     def free_slot(cal,time):
         busy, result = list(cal[0]) ,[]
         # bottom 
         if cal[0][0] != time[0]:
             result.append([time[0],cal[0][0]])
         for i in range(1,len(cal)):
             if cal[i][0] > busy[1]:
                 # add the free slot and update the busy time
                 # result.append([busy[1],cal[i][0]])
                 result.append([cal[i-1][1],cal[i][0]])
                 busy[1] = cal[i][1]
             else:
                 busy[1] = max( cal[i][1],busy[1])
        # put the lid on
         if cal[-1][1] != time[1]:
             result.append([cal[-1][1],time[1]])
         return result
     free1, free2 = free_slot(cal1,time), free_slot(cal2,time)
     index1 = index2 = 0
     while index1 < len(free1) and index2 < len(free2):
         startTime = max(free1[index1][0], free2[index2][0])
         endTime = min(free1[index1][1],free2[index2][1])
         # if the gap can hold the meeting then update the list
         if endTime - startTime >= duration:
             ans.append([startTime,endTime])
         if free1[index1][1] >= free2[index2][1]:
             index2 += 1
         else:
             index1 += 1
     print(ans)
     return ans 
calendar1 = [(0,100),(200,230),(250,330),(450,500)]
calendar2 = [(30,100),(100,130),(250,330)]
duration = 50
time = (0,500)
get_free_time(calendar1,calendar2,duration,time)

def removeComments(source):
    result = ""
    if not source:
        return result
    inBlock = False
    for line in source:
        if not inBlock:
            newLine = ''
        i = 0 
        while i < len(line):
            if line[i:i+2] == '/*' and not inBlock:
                inBlock = True 
                i += 1
            elif line[i:i+2] == '*/' and inBlock:
                inBlock = False
                i += 1
            elif line[i:i+2] == '//' and not inBlock:
                break
            elif not inBlock:
                newLine += line[i]
            i += 1
        if not inBlock and newLine:
            result += newLine
    print(result)
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source2 = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
removeComments(source)
removeComments(source2) # ab    