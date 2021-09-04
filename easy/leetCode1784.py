#1784. Check if Binary String Has at Most One Segment of Ones
def checkOnesSegment(s):
    count = 0
    if s == "1":
        return True
    for i in range(len(s)-1):
            if s[i] != s[i+1]:
                count += 1
    return True if count < 2 else False 


checkOnesSegment("1001")
checkOnesSegment("110")
checkOnesSegment("10")
checkOnesSegment("1011")
checkOnesSegment("1111")