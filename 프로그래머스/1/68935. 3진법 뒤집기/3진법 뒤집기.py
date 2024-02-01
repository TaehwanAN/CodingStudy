def solution(n):
    answer = ''
    # 1. n을 3진법 문자열로 변환하기
    ## s: 몫, r: 나머지
    s=n
    while True:
        s,r= divmod(s,3)
        answer= str(r)+answer
        if s==0:
            break
    # 2. 3진법->앞뒤반전
    answer=answer[::-1]
    answer=int(answer,3)
    return answer