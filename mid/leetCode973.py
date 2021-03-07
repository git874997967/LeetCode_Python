# 973. K Closest Points to Origin
def kClosest(self, points, k):
    points.sort(key = lambda P :P[0] ** 2 + P[1] **2 )
    return points[:k]

def kClosest2(self,points,k):
    heapq.nsmallest(k,points,lambda (x,y): x**2 + y**2 )


 