def solution(array, commands):
    answer = []
    ## 1. commands의 길이만큼 반복하여 커맨드 내부의 리스트의 원소를 각각 i,j,k로 받는다.
    for c in range(len(commands)):
        i,j,k=commands[c]

    # ## 2. 받은 i,j를 활용하여 array를 인덱싱한다.
        indexed_list=array[i-1:j]

    # ## 2-1. 인덱싱된 리스트를 정렬한다.
        indexed_list=sorted(indexed_list)

    # ## 3. k를 활용하여 특정 값을 찾고, 이를 정답지에 추가한다.
        answer.append(indexed_list[k-1])
    return answer