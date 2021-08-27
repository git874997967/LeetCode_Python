#1275. Find Winner on a Tic Tac Toe Game
from typing import DefaultDict
def tictactoe(moves):
     chess = [[0 for _ in range(3)]for _ in range(3)]
     sameCross,antiCross = 0, 0
     sameRow,sameCol = 0 , 0
     for step in range(len(moves)):
         r,c = moves[step][0], moves[step][1]
         chess[r][c] = -1 if step % 2 == 0 else -4
     for i in range(0,3):
         sameRow = chess[i][0] + chess[i][1] + chess[i][2]
         sameCol = chess[0][i] + chess[1][i] + chess[2][i]
         if sameCol == -3 or sameRow == -3: 
             return 'A'
         elif sameRow == -12 or sameCol == -12:
             return 'B'
         sameCross += chess[i][i]
         antiCross += chess[2-i][i]
         if sameCross == -3 or antiCross == -3:
             return 'A'
         elif antiCross == -12 or antiCross == -12:
             return 'B'
     if len(moves) == 9:
         return 'Draw'
     else:
         return 'Pending'
 

moves1= [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves2 = [[0,0],[1,1]]
moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves4 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]

print(tictactoe(moves1)) #a
print(tictactoe(moves2)) #"pending"
print(tictactoe(moves3)) #draw
print(tictactoe(moves4)) # B