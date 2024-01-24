def solution(score):
    answer = []
    ## 1.평균 담은 리스트
    avgs=[i for i in map(lambda x: sum(x)/len(x), score)]
    # print(avgs)
    ## 2.평균의 순위 비교: 내림차순 정렬, 공동순위 처리 어떻게?
    sort_avgs=sorted(avgs, reverse=True) 
    for n in avgs: # 평균 구한것들
        answer.append(sort_avgs.index(n)+1) # 내림차순 정렬에서 평균 값의 인덱스를 구함 # 어차피 평균이 같으면 내림차순에서 처음으로 발견되는 인덱스도 같아서 괜찮
    ## 3. 순위 담은 리스트
    return answer