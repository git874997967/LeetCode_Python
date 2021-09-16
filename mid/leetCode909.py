#909. Snakes and Ladders
# 5 [-1,-1,-1,-1,-1,-1],
# 4 [-1,-1,-1,-1,-1,-1],
# 3 [-1,-1,-1,-1,-1,-1],
# 2 [-1,35,-1,-1,13,-1],
# 1 [-1,-1,-1,-1,-1,-1],
# 0 [-1,15,-1,-1,-1,-1]]
#   0 1   2  3  4  5
def snakesAndLadders(board):
    rows, cols = len(board), len(board[0])
    start = board[rows-1][0]
    