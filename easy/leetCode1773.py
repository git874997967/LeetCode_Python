#1773. Count Items Matching a Rule
def countMatches(items, ruleKey, ruleValue):
    ruleMap = {"type":0,"color":1,"name":2}

    count ,rule = 0,ruleMap.get(ruleKey)
    for i in range(len(items)):
        item = items[i]
        if item[rule] == ruleValue:
            count += 1
    return count 