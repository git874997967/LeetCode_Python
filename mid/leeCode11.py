def maxArea(height):
    max_water = 0 
    i ,j = 0, len(height) - 1
    max_water = min(height[i], height[j]) * (j - i )
    while i < j :
        temp_max = min(height[i], height[j]) *(j - i)
        max_water = max(temp_max,max_water)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    print(max_water)
    return max_water

maxArea([1,8,6,2,5,4,8,3,7])
