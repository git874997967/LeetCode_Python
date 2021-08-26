#S = (1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
#1037. Valid Boomerang
def isBoomerang(points):
    x1, y1 = points[0][0],points[0][1]
    x2, y2 = points[1][0],points[1][1]
    x3, y3 = points[2][0],points[2][1]
    
    return (x1*y2 + x2*y3 + x3*y1 - x1*y3 -x2*y1 - x3*y2) != 0