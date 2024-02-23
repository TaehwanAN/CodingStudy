def solution(id_list, report, k):
    answer = []
    ## 알고리즘 분석
    # 0. report를 집합으로 바꿔서 중복을 없애주는 전처리 필요
    # 1. id_list를 가지고 reporter와 reported 딕셔너리를 만든다.
    # 2. report를 순회하면서, 각 원소를 스플릿하고 reported 된 사람의 카운트를 올려준다.
    # 3. reported count가 k 이상인 사람들을 확인한다.
    # 4. report를 순회하면서 k 이상인 사람을 지목한 사람의 reporter 카운트를 올려준다.
    # 5. reporter의 숫자를 리스트로 반환한다. 
    report=set(report)
    reporter={}
    reported={}
    suspension=[]
    for i in id_list:
        reporter[i]=0
        reported[i]=0
    
    for r in report:
        v=r.split(' ')
        reported[v[1]]+=1
    
    for n,v in reported.items():
        if v>=k:
            suspension.append(n)
    
    for r in report:
        v=r.split(' ')
        if v[1] in suspension:
            reporter[v[0]]+=1
    
    for i in id_list:
        answer.append(reporter.get(i,0))
    
    return answer