def maxWidthOfVerticalArea(points):
    sort_points = sorted(points , key = lambda x:x[0])
    max_width = 0
    init_x = sort_points[0][0]
    for point in sort_points:
        next_x = point[0]
        max_width = max(max_width, abs(next_x - init_x))
        init_x  = next_x
        
    print(max_width)
    
maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])


maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])