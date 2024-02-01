def solution(arr1, arr2):
    answer = []
    for row1,row2 in zip(arr1,arr2):
        v_list=[]
        for v1,v2 in zip(row1,row2):
            v_list.append(v1+v2)
        answer.append(v_list)
    return answer