# 599. Minimum Index Sum of Two Lists
def findRestaurant(list1, list2):
    result, restMap , minIndex = [], {val:index for index , val in enumerate(list1)}, float('inf')
    commMap = {}
    for index,val in enumerate(list2):
        if val in restMap:
            commMap[val] = index + restMap[val]
            minIndex = min(minIndex, commMap[val])
    result = [key for key in commMap.keys() if commMap[key] == minIndex]
    return result

def findRestaurant2(list1,list2):
    res, restMap, minIndex = [], {val:key for key,val in enumerate(list1)}, float('inf')
    for index, val in enumerate(list2):
        if val in restMap:
            if restMap[val] + index < minIndex:
                minIndex = index + restMap[val]
                res = [val]
            elif restMap[val] + index == minIndex:
                res.append(val)
    return res
print(findRestaurant2(["Shogun","Tapioca Express","Burger King","KFC"],  ["KFC","Shogun","Burger King"])) 
    

print(findRestaurant2(["Shogun","Tapioca Express","Burger King","KFC"],  ["KNN","KFC","Burger King","Tapioca Express","Shogun"])) 
    
