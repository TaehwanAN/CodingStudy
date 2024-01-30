def solution(seoul):
    answer = ''
    for i, v in enumerate(seoul):
        if "Kim" in v:
            answer=f'김서방은 {i}에 있다'
            break
    return answer