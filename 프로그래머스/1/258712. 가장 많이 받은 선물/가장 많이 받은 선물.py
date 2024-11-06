def solution(friends, gifts):
    gift_table = {}
    get_table = {friend : 0 for friend in friends}
    point_table = {friend : 0 for friend in friends}
    
    for gift in gifts:
        tmp = str.split(gift)
        cvy = tmp[0]
        clby = tmp[1]
        try:
            gift_table[cvy][clby] += 1
        except:
            try:
                gift_table[cvy][clby] = 1
            except:
                gift_table[cvy] = {clby : 1}
        point_table[cvy] += 1
        point_table[clby] -= 1
    
    for cvy in friends:
        for clby in friends:
            if cvy == clby:
                continue
            try:
                cvy_count = gift_table[cvy][clby]
            except:
                cvy_count = 0
            try:
                clby_count = gift_table[clby][cvy]
            except:
                clby_count = 0
            if cvy_count > clby_count:
                get_table[cvy] += 0.5
                
            elif cvy_count < clby_count:
                get_table[clby] += 0.5
                
            else:
                cvy_point = point_table[cvy]
                clby_point = point_table[clby]
                
                if cvy_point == clby_point:
                    continue
                elif cvy_point > clby_point:
                    get_table[cvy] += 0.5
                    
                else:
                    get_table[clby] += 0.5
    answer = max(list(get_table.values()))
    return answer