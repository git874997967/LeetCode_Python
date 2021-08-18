# 836. Rectangle Overlap
def isRectangleOverlap(rec1, rec2):
     # get the distance 
    x1=rec1[0] 
    x3=rec2[0]
    y1=rec1[1] 
    y3=rec2[1]
    x2=rec1[2] 
    x4=rec2[2]
    y2=rec1[3] 
    y4=rec2[3]

    return (min(x2,x4)>max(x1,x3)) and (min(y2,y4)>max(y1,y3))

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(isRectangleOverlap(rec1,rec2))