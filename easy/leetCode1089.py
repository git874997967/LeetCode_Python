#1089. Duplicate Zeros
def duplicateZeros( arr):
    que = []
    for i in range(len(arr)):
        que.append(arr[i])
        if arr[i] == 0:
            que.append(0)
        arr[i] = que.pop(0)
        print(que)
    print(arr)

    
duplicateZeros([1,0,2,3,0,4,5,0])