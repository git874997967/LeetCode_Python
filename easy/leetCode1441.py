#1441. Build an Array With Stack Operations
def buildArray(target, n):
    result = []
    for i in range(len(target)):
        if len(result) == 0:
            init = target[0]
            if init == 1:
                result.append("Push")
            else:
                while init > 1:
                    result.append("Push")
                    result.append("Pop")
                    init -= 1
                result.append("Push")
        else:
            diff = target[i] - target[i-1]
            if diff == 1:
                result.append("Push")
            else:
                while diff > 1:
                    result.append("Push")
                    result.append("Pop")
                    diff -= 1
                result.append("Push")
       
             
    print(result)
    return result

buildArray([2,3,4],4)
buildArray([1,2],4)
buildArray([1,2,3],3)
buildArray([1,3],4)