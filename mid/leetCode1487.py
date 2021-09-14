#1487 Making file Names unique
def getFolderNames(names):
#["gta","gta(1)","gta(2)","avalon()","avalon()"]
#["gta","gta(1)","gta(2)","avalon()","avalon()(1)"]
#      
    nameCount,result = {},[]
    for name in names:
         modified = name
         if name in nameCount:
             k = nameCount[name]
             while modified in nameCount:
                 k += 1
                 modified = name + "(" + str(k) + ")"
             nameCount[name] = k
         nameCount[modified] = 0
         result.append(modified)
    print(result)
    return result


 

getFolderNames(["gta","gta","gta(1)","gta(2)"])