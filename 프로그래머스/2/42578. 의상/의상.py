# def solution(clothes):
#     answer = 0
#     ## clothes를 어떤 자료구조로 변경할 것인가
#     # 딕셔너리?
#     clothes_dic={}
#     for i in clothes:
#         if clothes_dic.get(i[1],None)==None:
#             clothes_dic[i[1]]=[]        
#         clothes_dic[i[1]].append(i[0])
#         answer+=1
#     # print(clothes_dic)
#     # print(len(clothes_dic))

#     combi=1
#     for key, value in clothes_dic.items():
#         combi*=len(value)
#     answer+=combi
#     return answer


def solution(clothes):
    clothes_dic = {}
    for i in clothes:
        if i[1] not in clothes_dic:
            clothes_dic[i[1]] = []        
        clothes_dic[i[1]].append(i[0])

    answer = 1
    for key, value in clothes_dic.items():
        answer *= (len(value) + 1) ## 안입는 것도 경우의 수로 고려하려고 1 추가

    return answer - 1 ## 전부 다 안입는 거는 안되니까 1 뺴기