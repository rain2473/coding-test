def solution(wallpaper):
    left, right, up, down = 51, -1, 51, -1
    for i, wp in enumerate(wallpaper):
        if "#" in wp:
            up = min(up, i)
            down = max(down,i)
            left = min(left, wp.find("#"))
            right = max(right, wp.rfind("#"))
    answer = [up, left, down + 1, right + 1]
    return answer