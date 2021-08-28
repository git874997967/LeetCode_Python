#1346. Check If N and Its Double Exist
def checkIfExist(arr):
     
    for num in arr:
        if num * 2 in arr:
            return True
    return False