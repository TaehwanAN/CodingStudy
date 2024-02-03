def solution(k, score):
    answer = []
    honor=[]
    ## honor에는 명예의 전당에 들어온 점수들을 내림차순으로 보관한다.
    ## answer에는 매 번 honor의 마지막 값을 추가한다.
    ## honor는 최대 길이 k이며, k 초과 시 새로 들어올 값과 k의 마지막 값을 비교하여 삭제 및 추가한다.
    for s in score:
        honor.append(s)
        honor=sorted(honor, reverse=True)
        if len(honor)>k:
            honor.pop()
        answer.append(honor[-1])
            
    return answer