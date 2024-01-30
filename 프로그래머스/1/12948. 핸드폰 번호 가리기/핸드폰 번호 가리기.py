def solution(phone_number):
    answer = ''
    for i, n in enumerate(phone_number):
        if i<len(phone_number)-4:
            answer+='*'
        else:
            answer+=n
    return answer