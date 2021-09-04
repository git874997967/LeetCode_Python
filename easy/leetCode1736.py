#1736. Latest Time by Replacing Hidden Digits
def maximumTime(time):
        if time.count("?") == 0:
            return time
        timeArr = time.split(":")
        result = ""
        if timeArr[0] == "2?" or timeArr[0] == "??":
            result += "23"
        elif timeArr[0] == "1?":
            result += "19"
        elif timeArr[0] == "0?":
            result += "09"
        elif timeArr[0][0] == "?":
            if timeArr[0][1] in "0123":
                result += "2" + timeArr[0][1]
            else:
                result += "1" + timeArr[0][1]
        else:
            result += timeArr[0]
        result += ":"
        if timeArr[1] == "??":
            result += "59"
        elif timeArr[1][1] == "?":
            result += timeArr[1][0] + '9'
        elif timeArr[1][0] == '?':
            result += '5' + timeArr[1][1]
        else:
            result += timeArr[1]

        return result

