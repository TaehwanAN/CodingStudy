# def solution(N, stages):
#     answer = []
    ## 알고리즘 고민
    # 1. 스테이지의 개수 만큼 반복한다
    # 2. 스테이지(n)와 같은 값의 갯수를 센다 = onstage_users
    # 3. challenging_users를 도전한 사람의 수로 나눈다 = failure_rate
    # 4. failure_rate과 스테이지(n)를 키와 밸류로 저장한다.
    # 5. stages에서 n을 제외시켜준다.
    # 6. 저장된 키와 밸류를 내림차순으로 정렬한다. (그러므로 일단 모든 키의 밸류에 0을 넣어둔다.)
    # 참고로, 밸류가 같다면 키의 값을 기준으로 정렬한다.
    
    ## 다른 방식
    # 1. 스테이지의 개수(N) 만큼 반복한다.
    # 2. '현 스테이지(n)와 같은 사람의 수'를 '현 스테이지와 같거나 큰 사람의 수'로 나눈다.
    # 딕셔너리로 저장하여 정렬 반환하는 것은 상동
    
    #### 굳이 딕셔너리로 안만들고, 튜플 형태로 리스트에 추가해줘도 될듯
#     for n in range(1,N+1):
#         onstage_users=0
#         challenge_users=0
        
#         onstage_users=stages.count(n)
#         for s in stages:
#             if s>=n:
#                 challenge_users+=1
#         failure_rate=onstage_users/challenge_users
#         answer.append(tuple((n,failure_rate)))
#         print(n,failure_rate)
#     answer=[t[0] for t in sorted(answer, reverse=True, key=lambda x: x[1])]
#     # # sorted(failure_dict,key=lambda x: failure_dict.items[1], reverse=True)
#     # answer=list(failure_dict)
        
#     return answer

#### 위의 코드로는 런타임 에러가 발생한다.
## 아마도 스테이지에 도달한 사람이 없는 경우를 고려하지 못해서인듯. 왜냐면 스테이지 도달한 사람이 없으면, challenging_users=0 이라 분모가 0이 되어 버리기 때문.
def solution(N, stages):
    answer = []
    for n in range(1,N+1):
        onstage_users=0
        challenge_users=0
        
        onstage_users=stages.count(n)
        for s in stages:
            if s>=n:
                challenge_users+=1
        ## 스테이지 도달 못한 경우 고려한 코드 삽입
        if challenge_users==0:
            failure_rate=0
        else:
            failure_rate=onstage_users/challenge_users
        answer.append(tuple((n,failure_rate)))
        # print(n,failure_rate)
    answer=[t[0] for t in sorted(answer, reverse=True, key=lambda x: x[1])]
        
    return answer
