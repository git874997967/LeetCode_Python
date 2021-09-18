def ArrayChallenge(strArr):
    result = leveToPre(strArr,0,0)
def leveToPre(arr,ind,newArr):
    if ind >= len(arr):
        return newArr
    newArr.append(arr[ind])
    newArr = leveToPre(arr,ind* 2 + 1,newArr)
    newArr = leveToPre(arr,ind * 2 + 2,newArr)
    return newArr

# keep this function call here 

strArr = "ABCDEDQCZCCCCCA"

print(ArrayChallenge(strArr))