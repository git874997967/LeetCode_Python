def convertTime(crrent,correct):
    current_hour,current_min = int(current.split(':')[0]), int(current.split(':')[1])
    correct_hour,correct_min = int(correct.split(':')[0]), int(correct.split(':')[1])
    
    step = 0 
    
    if correct_hour > current_hour and correct_min < current_min:
        hour_step = correct_hour - current_hour - 1 
        min_gap = (correct_min + 60 - current_min)
        