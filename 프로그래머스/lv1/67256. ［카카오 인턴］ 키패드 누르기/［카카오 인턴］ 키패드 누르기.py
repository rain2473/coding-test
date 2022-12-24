def solution(numbers, hand):
    left, right, answer = 9, 11, ""
    for i in numbers:
        i -= 1
        if i == -1:
            i = 10
        dis_left = abs(i%3 - left%3) + abs(left//3 - i//3)
        dis_right = abs(right%3 - i%3) + abs(right//3 - i//3)
        if i in [0,3,6]:
            answer += "L"
            left = i
        if i in [2,5,8]:
            answer += "R"
            right = i
        if i in [1,4,7,10]:
            if dis_left < dis_right:
                answer += "L"
                left = i
            elif dis_left > dis_right:
                answer += "R"
                right = i
            else:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i
    return answer