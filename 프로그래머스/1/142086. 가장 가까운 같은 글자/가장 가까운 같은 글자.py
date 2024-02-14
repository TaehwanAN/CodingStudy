def solution(s):
    ## 알고리즘 분석
    # 리스트 구조 사용
    # s 순회
    # 1.1 리스트에 자기 자신 없으면 스택에 추가.
    # 1.1 answer 에 -1 추가.
    # 1.2 리스트에 자기 자신이 있는 경우
    # 1.2.1 리스트에 자기자신을 추가
    # 1.2.2 리스트를 순회하면서 가장 가까운 인덱스 갱신 
    # 1.2.3 answer에 추가: 자신의 인덱스(리스트 길이 -1 ) - 마지막으로 갱신되었던 인덱스
    answer = []
    s_list=[]
    for i in s:
        if i not in s_list:
            s_list.append(i)
            answer.append(-1)
        else:
            s_list.append(i)
            nearest_idx=0
            for j,l in enumerate(s_list[:-1]):
                if i==l:
                    nearest_idx=j
                # print(nearest_idx)
                # 확인결과 s_list의 가장 마지막은 자기 자신인데 여기까지 순회하다보니 항상 0이 발생했던것. 따라서 s_list[:-1] 까지만 순회
            answer.append(len(s_list)-1-nearest_idx)
            # print(s_list) 
    return answer