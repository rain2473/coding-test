def solution(w,h):
    answer = w * h
    unable = 0
    x_coor = 0
    y_coor = 0
    
    if min(w, h) == 1:
        return 0
    
    while 1:
        pre_x_coor = x_coor
        pre_y_coor = y_coor

        x_coor += 1
        y_coor = x_coor * h / w
        
        unable += (int(y_coor) - int(pre_y_coor))
        
        if x_coor == w or y_coor == h:
            break
        
        if int(y_coor) == y_coor:
            break
        unable += 1
    
    answer -= unable * int(w / x_coor)
    
    return answer