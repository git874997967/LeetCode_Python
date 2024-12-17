def maxDistance(colors):
    
    result = 0 
    size = len(colors)
    for i, color in enumerate(colors):
        size = len(colors) - 1
        while size > i:
            if color != colors[size]:
                print(size, i,colors[size], colors[i],result)
                result = max(result,  size - i )
                break 
            else:
                size -= 1
    print(result)
    
    
    
maxDistance([1,8,3,8,3])
maxDistance([4,4,4,11,4,4,11,4,4,4,4,4])
maxDistance([1,1,1,6,1,1,1])