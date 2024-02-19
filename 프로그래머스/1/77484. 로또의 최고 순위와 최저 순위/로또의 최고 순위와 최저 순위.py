def solution(lottos, win_nums):
    answer = []
    ## 알고리즘 분석:
    # 가능한 순위를 담는 rank 변수 만든다.
    # 1. 일단 lottos에서 0을 제외하고 0의 개수만 체크해둔다.
    # 2. lottos를 순회하며, win_nums에 원소가 있는지를 확인한다.
    # 3. 최종 rank+0의 갯수=최고순위, 최저순위는 rank
    zero_cnt=lottos.count(0)
    rank=7
    for l in lottos:
        # if l==0: continue
        if l in win_nums:
            rank-=1
    answer.append(rank-zero_cnt if rank-zero_cnt<=6 else 6)
    answer.append(rank if rank<=6 else 6)
    return answer