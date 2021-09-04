#1812. Determine Color of a Chessboard Square
def squareIsWhite(coordinates):
    row,col = coordinates[0],coordinates[1]
    if row in "aceg":
        return True if col % 2 == 1 else False
    else:
        return False if col % 2 == 1 else True 