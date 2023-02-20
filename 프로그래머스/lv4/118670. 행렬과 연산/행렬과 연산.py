from collections import deque
def solution(rc, operations):
    left, right, body = seperate(rc)
    for operation in operations:
        if operation == "Rotate":
            left, right, body = rotate(left, right, body)
        else:
            left, right, body = ShiftRow(left, right, body)
    rc = merge(left, right, body)
    return rc

def seperate(rc):
    left, right, body = deque(), deque(), deque()
    rc = deque(rc)
    while rc:
        row = rc.popleft()
        row = deque(row)
        l = row.popleft()
        r = row.pop()
        left.append(l)
        right.append(r)
        body.append(row)
    return left, right, body

def merge(left, right, body):
    rc = []
    while left:
        l = left.popleft()
        r = right.popleft()
        try:
            b = body.popleft()
        except:
            pass
        row = [l] + list(b) + [r]
        rc.append(row)
    return rc

def rotate(left, right, body):
    top, bottom = body.popleft(), body.pop()
    r = right.pop()
    l = left.popleft()
    try:
        t = top.pop()
        b = bottom.popleft()
        top.appendleft(l)
        right.appendleft(t)
        left.append(b)
        bottom.append(r)
    except:
        right.appendleft(l)
        left.append(r)
    body.appendleft(top)
    body.append(bottom)
    return left, right, body

def ShiftRow(left, right, body):
    left.rotate(1)
    right.rotate(1)
    body.rotate(1)
    return left, right, body