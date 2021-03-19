#1229. Meeting Scheduler
def minAvailableDuration(slot1,slot2,duration):
    slot1.sort()
    slot2.sort()
    pointer1 = pointer2 = 0
    while pointer1 < len(slot1) and pointer2 < len(slot2) :
        #bounderies of the intersaction or the common slot
        intersect_right = min(slot1[pointer1][1], slot2[pointer2][1])
        intersect_left = max(slot1[pointer1][0],slot2[pointer2][0])
        if intersect_right - intersect_left >= duration:
            return [intersect_left , intersect_left + duration]
        if slot1[pointer1][1] < slot2[pointer2][1]:
            pointer1 += 1
        else :
            pointer2 += 1
    return result

 