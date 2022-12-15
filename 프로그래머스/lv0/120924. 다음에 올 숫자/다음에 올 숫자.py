def solution(common):
    try:
        return (common[-1]-common[-2]+common[-1])*(common[-3] + common[-1] == common[-2]*2) + (common[-1]/common[-2]*common[-1])*(common[-3] * common[-1] == common[-2]**2) * (common[-1] != common[-2])
    except:
        return (common[-1]-common[-2]+common[-1])*(common[-3] + common[-1] == common[-2]*2)
        