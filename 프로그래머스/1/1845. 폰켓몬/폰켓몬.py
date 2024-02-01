def solution(nums):
    answer = 0
    ## HashSet을 사용하면 리스트의 유니크한 값들만 취할 수 있음.
    # 유니크한 값의 개수: 가져갈 수 있는 폰켓몬의 종류 개수
    # 그러나 홍박사의 제한으로 인해 절반만 가져갈 수 있음.
    # 따라서 아무리 종류가 많아도 최대 가져갈 수 있는 종류의 수는 절반으로 제한됨.
    if len(set(nums)) > len(nums)/2:
        answer= len(nums)/2
    else:
        answer= len(set(nums))
    
    return answer