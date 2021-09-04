#1725. Number Of Rectangles That Can Form The Largest Square
def countGoodRectangles(rectangles):
    result, curMax = 0,0
    for rectangle in rectangles:
        sideLength = min(rectangle[0],rectangle[1])
        if sideLength == curMax:
            result += 1
        elif sideLength > curMax:
            result = 1
            curMax = sideLength

    return result