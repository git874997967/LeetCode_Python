#1854. Maximum Population Year
def maximumPopulation(logs):
    popArr,maxPop = [0] * 100, 0
    for log in logs:
        birth,die = log[0],log[1]
        for i in range(birth,die):
            popArr[i - 1950] += 1
            maxPop = max(maxPop, popArr[i - 1950])
    return popArr.index(maxPop) + 1950