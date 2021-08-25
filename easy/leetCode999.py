#999. Available Captures for Rook
def numRookCaptures(board): # edge detection
    rootX, rootY = 0,0
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    result = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rootX,rootY = i , j 
                break

    for x,y in dirs:
        newX, newY = rootX + x, rootY + y
        while 0 <= newX < 8 and 0 <= newY < 8:
            if board[newX][newY] == 'p':
                result += 1
            if board[newX][newY] != '.':
                break
            newX , newY = newX + x, newY + y
    return result