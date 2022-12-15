def solution(rsp):
    return "".join([str(2*(i=="5") + 5*(i=="0")) for i in list(rsp)])