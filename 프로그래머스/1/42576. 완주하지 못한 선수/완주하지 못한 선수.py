# def solution(participant, completion):
#     # answer = list(set(participant) - set(completion))[-1]
    
#     ## set을 통해 접근하는 경우, 동명이인의 참가자 중에서 completion하지 못한 사람은
#     # 구할 수가 없다.
#     p_dict={}
#     for p in set(participant): # 참가자들 유니크 값만큼 반복 O(n)
#         p_dict[p]=participant.count(p) 
#     for c in set(completion): # 완주자들 유니크 값만큼 반복 
#         p_dict[c]-=completion.count(c)
    
#     for k,v in p_dict.items():
#         if v==1:
#             answer=k
#             break

#     for c in completion:
#         participant.remove(c)
#     answer=participant[0]
    
    
    
#     return answer


from collections import Counter
## Counter 사용시 리스트의 값을 각각 {키:빈도}로 변환해준다.

def solution(participant, completion):
    participant_count = Counter(participant)
    # participant_count={"p1":1, "p2":2,"p3":1,"p4":1...}
    completion_count = Counter(completion)

    for p, count in participant_count.items():
        if count != completion_count.get(p, 0): ## 핵심 알고리즘
            return p
        ## 참가자 딕셔너리의 키(이름)와 밸류(빈도)를 순회함.
        # 참가자의 키를 가지고 완주자 딕셔너리의 키를 뒤져봄.
        # 참가자 빈도수와 완주자 빈도수 다르면, 그 참가자 반환함.