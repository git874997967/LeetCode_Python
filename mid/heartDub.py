# convert levelorder into preorder
def ArrayChallenge(strArr):
    result  = levelToPre(strArr,0,[])
    return " ".join([i for i in result if i != '#' ])

def levelToPre(arr,index,newArr):
    if index > len(arr):
        return newArr
    newArr.append(arr[index])
    newArr += levelToPre(arr,index * 2 + 1, newArr)
    newArr += levelToPre(arr,index * 2 + 2, newArr)
    return newArr
