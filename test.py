def removeDupliates(arr1,arr2):
    dict = {}
    for num in arr1:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    for num in arr2:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    result = [ k  for k in dict.keys() if dict[k] == 1]
    return result
arr1 = [1,2,3,4,2,5]
arr2 = [1,3,5,7,9]
print(removeDupliates(arr1,arr2))