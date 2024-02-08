def solution(arr):
    answer = []
    ## 알고리즘 분석:
    # 스택형. 일단 arr의 원소 넣고, 이미 들어간 원소와 새로 들어올 원소가 같지 않을 경우에만, 삽입
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
            
    return answer