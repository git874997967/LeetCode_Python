#1213. Intersection of Three Sorted Arrays
def arraysIntersection(arr1, arr2, arr3):
     result = []
     p1,p2,p3, l1,l2,l3 = 0,0,0,len(arr1),len(arr2),len(arr3)

     while p1 < l1 and p2 < l2 and p3 < l3:
         if arr1[p1] == arr2[p2] == arr3[p3]:
             result.append(arr1[p1])
             p1 += 1
             p2 += 1
             p3 += 1
         else:
            if arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            else:
                p3 += 1

     return result
