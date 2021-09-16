#1197. Minimum Knight Moves
def minKnightMoves(x, y):
     def dfs(x,y):
         if x + y == 0:
             return 0
         elif x + y == 2:
             return 2 
         else:
            return min(dfs(abs(x-1),abs(y-2)) , dfs(abs(x-2),abs(y-1)) + 1            )
     
     
     return dfs(x,y)

def minKnightMoves2(x,y):
        x, y = abs(x), abs(y)
        if (x < y): x, y = y, x
        if (x == 1 and y == 0): return 3        
        if (x == 2 and y == 2): return 4        
        delta = x - y
        if (y > delta):
            return delta - 2 * ((delta - y) // 3);
        else:
            return delta - 2 * ((delta - y) // 4);

# minKnightMoves(2,1)

# minKnightMoves(5,5)

minKnightMoves(130,-86)
minKnightMoves(300,0)