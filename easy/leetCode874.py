# 874. Walking Robot Simulation
def robotSim(commands, obstacles):
     obstacles = {(x,y) for x,y in obstacles}
     dist = 0
     x,y, = 0,0
     dx,dy = 0,1 # face to North first 

     for move in commands:
         if move == -2:
             dx, dy = -dy, dx 
         if move == -1 :
             dx, dy = dy, -dx 
         else:
             for i in range(move):
                 if (x + dx, y + dy) in obstacles:
                     break
                 x, y = x + dx, y + dy 
             dist = max(dist , x* x + y * y )
     return dist

def robotSim2(commands, obstacles):
    m,x,y = 0,0,0
    direction = 0
    O = {tuple(o): None for o in obstacles}
    for c in commands:
        # the direction has 4 possibles  0 north 1 east 
        if c == -1:
            direction = (direction + 1) % 4
        elif c == -2:
            direction = (direction -1) % 4
        else:
            if direction == 0: # face North
                for i in range(c):
                    y += 1
                    if (x,y)in O:
                        y -= 1
                        break
            elif direction == 1: # face East
                for i in range(c):
                    x += 1
                    if (x,y) in O:
                        x -= 1
                        break
            elif direction == 2: # face South
                for i in range(c):
                    y -= 1
                    if (x,y) in O:
                        y += 1
                        break
            else:             # face West
                for i in range(c):
                    x -= 1
                    if(x,y) in O:
                        x += 1
                        break
        m = max(m, x **2 + y **2)
    print(m)
    return m
                    
commands = [-2,-1,8,9,6]
obstacles = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]
commands1 = [4,-1,4,-2,4]
obstacles1 = [[2,4]]
robotSim2(commands1, obstacles1)
