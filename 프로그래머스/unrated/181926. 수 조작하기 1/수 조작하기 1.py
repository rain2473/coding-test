def solution(n, control):
    for s in control:
        n += 1 * (s == 'w') - 1 * (s == 's') + 10 * (s == 'd') - 10 * (s == 'a')
    return n