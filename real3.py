def removeComments(source):
    if not source:
        return source
    result ,inBlock = "", False
    for line in source:
        if not inBlock:
            newLine = ""
        char = 0
        while char in range(len(line)):
            if line[char:char+2] == '/*' and not inBlock:
                inBlock = True
                char += 1
            elif line[char:char+2] == '*/' and inBlock:
                inBlock = False
                char += 1
            elif line[char:char+2] =='//' and not inBlock:
                break
            elif not inBlock:
                newLine += line[char]
            char += 1
        if not inBlock and newLine:
            result += newLine 

    print(result)
    return result
def get_free_time(cal1,cal2,duration,time):
    ans = []
    def get_free(cal, time):
        # base case
        if not cal:
            return time
        cal = sorted(cal, key = lambda x:x[0])
        freeTime, busy= [],list(cal[0])
        # add the bottom
        if cal[0][0] != time[0]:
            freeTime.append([time[0],cal[0][0]])
        # put other free slots 
        for index in range(1, len(cal)):
            if cal[index][0] > busy[1]:
                freeTime.append([busy[1],cal[index][0]])
                busy[1] = cal[index][1]
            else:
                busy[1] = max(busy[1], cal[index][1])
        # put the lid
        if cal[-1][1] != time[1]:
            freeTime.append([cal[-1][1],time[1]])
        return freeTime
    free1,free2 = get_free(cal1,time), get_free(cal2,time)
    print(free1,free2)
    indexi , indexj = 0,0
    while indexi < len(free1) and indexj < len(free2):
        startTime = max(free1[indexi][0],free2[indexj][0])
        endTime = min(free1[indexi][1],free2[indexj][1])
        if endTime - startTime >= duration:
            ans.append([startTime,startTime + duration])
        if free1[indexi][1] >= free2[indexj][1]:
            indexj += 1
        else:
            indexi += 1
    print(ans)
    return ans 

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source2 = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
removeComments(source)
removeComments(source2) # ab    
