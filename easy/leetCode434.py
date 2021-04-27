# 434. Number of Segments in a String
def countSegments(s):
    result = 0
    if len(s) == 0:
        return result
    if len(s) == 1 and s != ' ':
        return 1
    segment = False
    for i in range(len(s)):
        if (i == 0 or s[i -1] == ' ') and s[i] != ' ':
             result += 1
    return result