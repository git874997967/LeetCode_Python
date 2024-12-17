def findClosetNumber(nums):
    gap = float('inf')
    result = 0
    for num in nums:
        if abs(num) == gap:
             if num >= result:
                 result = num
             else:
                 continue 
        elif abs(num) < gap:
            result = num
            gap = abs(num)
        else:
            continue
    return result

        