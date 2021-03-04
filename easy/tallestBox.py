def tallestBox(boxes):
    # sort the boxes by the length x[0]
    boxes.sort(lambda x: x[0])
    # generate one dict  
    heights = {box: box[2] for box in boxes}
    for i in len(boxes):
        box = boxes[i]
        # S is the height untill now changeable 
        S = [box[j] for j in range(i) if canBeStaked(box[j], box)]
        # update the dict 
        heights[box] = box[2] + max([heights[box] for box in S], default = 0)
        return max(heights.values(), default = 0)
def canBeStaked(top, bottom):
    return top[0] < bottom[0] and top[1] < bottom[1]