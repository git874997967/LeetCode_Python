#1232. Check If It Is a Straight Line
def checkStraightLine(self, coordinates):
    for i in range(len(coordinates) - 2):
        x1, y1 = coordinates[i][0],coordinates[i][1]
        x2, y2 = coordinates[i+1][0],coordinates[i+1][1]
        x3, y3 = coordinates[i+2][0],coordinates[i+2][1]

        if (x1* y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1) != 0:
            return False
    return True