def solution(phone_number):
    return "".join(["*" for i in range(len(phone_number)-4)]+list(phone_number)[-4:])