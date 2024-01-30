def solution(n, arr1, arr2):
    answer = []
    ## arr1의 원소의 값을 5자리 이진수로 각각 변환하여, 문자열로 만든다. 
    # arr2도 동일한 작업을 한다.
    # 두 이중리스트를 묶어서 순회하면서, 둘 중 하나에서라도 1일 경우, #을 둘다 0일 경우 공백을 추가한다.

    # 자연수를 (다섯자리의) 이진수로 변환하기
    # zfill(n): n의 자리수로 만들되 빈칸은 zero를 채워라
    arr1_bin=[]
    arr2_bin=[]
    for i,j in zip(arr1,arr2):
        arr1_bin.append(str(bin(i)[2:].zfill(n)))
        arr2_bin.append(str(bin(j)[2:].zfill(n)))
        
    # 두 배열을 순회하면서 샵/공백 만들기
    for i_bin,j_bin in zip(arr1_bin,arr2_bin):
        shop_str=''
        shop_list=[]
        for i, j in zip(i_bin,j_bin):
            if (i=='1')or(j=='1'):
                shop_list.append('#')
            else:
                shop_list.append(' ')
        shop_str=''.join(shop_list)
        answer.append(shop_str)
    
    return answer