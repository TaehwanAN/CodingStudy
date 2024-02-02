def solution(food):
    answer = ''
    ## 인덱스가 (원소//2)만큼 반복 된다
    for index, value in enumerate(food):
        if index==0: continue
        elif value//2<1: continue
        else: answer+=str(index)*(value//2)
    answer_rev=answer[::-1]
    answer=answer+'0'+answer_rev
    return answer