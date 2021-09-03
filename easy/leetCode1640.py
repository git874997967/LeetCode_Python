#1640. Check Array Formation Through Concatenation
def canFormArray(arr, pieces):
    contain = len(pieces)
    for piece in pieces :
        lenPiece = len(piece)
        for i in range(0,len(arr) +1 - lenPiece, 1):
            if arr[i:i + lenPiece] == piece:
                contain -= 1
    return True if contain == 0 else False
arr = [75,1,60,91,84,55,5,39,19,52,38,66,14,17,49]
pieces = [[60],[52,38],[66],[39],[19],[1],[84,55],[17],[14],[49],[91],[5],[75]]
print(canFormArray(arr,pieces)) #True

arr = [15,88]
pieces = [[88],[15]] 
print(canFormArray(arr,pieces))  # True

arr = [49,18,16]
pieces = [[16,18,49]]
print(canFormArray(arr,pieces)) #False 

arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
print(canFormArray(arr,pieces)) # True 

arr = [32,66,73,15,3,70,53]
pieces = [[66,73],[15],[3],[32],[70],[53]]
print(canFormArray(arr,pieces)) # true
