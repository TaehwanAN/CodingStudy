def solution(d, budget):
    answer = 0
    d.sort() # 신청금액을 오름차순으로 정렬
    for i in d:
        if i>budget:
            break # 만약 신청금액이 남은 예산보다 더 크다면, 중지
        budget-=i # 신청금액에 대하여 예산 사용
        answer+=1 # 지원된 부서 횟수 +1
    return answer