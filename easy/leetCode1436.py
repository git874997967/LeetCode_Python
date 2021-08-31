#1436. Destination City
def destCity(paths):
    destMap = {}
    for path in paths:
        destMap[path[0]] = path[1]
    
    for path in paths:
        if path[1] not in destMap.values():
            return path[1]

    return ""
