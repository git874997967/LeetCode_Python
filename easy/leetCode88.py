# 88. Merge Sorted Array
# reverse : confirm the last element  and then move forward
def merge( n1 , n2, m, n):
    end1 , end2 = m -1 ,n -1 
    pointer = m + n - 1
    while end1 >= 0 and end2 >= 0:
        if n1[end1] > n2[end2]:
            n1[pointer] = n1[end1]
            end1 -= 1
        else:
            n1[pointer] = n2[end2]
            end2 -= 1
        pointer -= 1
    while end2 >= 0:
        n1[pointer] = n2[end2]
        end2 -= 1
        pointer -= 1


        
