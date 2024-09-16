# 두 큐의 합을 구하여, 절반을 target으로 잡는다.
# 두 큐 중 target보다 큰 큐에서 target보다 작은 큐로 보낸다
# 두 큐가 target과 각각 동일한지를 비교한다.
# 수행횟수를 1 증가 시킨다.
# 두 큐 중 어느 한쪽의 len==0 되는 순간 -1을 반환한다.

#### 시간초과가 발생하는 코드
### sum(list)가 O(n)의 시간복잡도이므로, 변수에 할당하고, pop된 원소를 더하거나 빼는 방식으로 고고
# 무한루프 도는 경우가 있음 => 탐색범위의 제한을 둘 필요가 있음
# def get_target(queue1, queue2):
#     return int((sum(queue1)+sum(queue2))/2)

# def proc_comparison(queue1, queue2, target):
#     cnt=0
#     sum_q1 = sum(queue1)
#     sum_q2 = sum(queue2)
    
#     while True:
#         if sum_q1<sum_q2:
#             q=queue2.pop(0)
#             queue1.append(q)
#             sum_q2-=q
#             sum_q1+=q
#         elif sum_q1>sum_q2:
#             q=queue1.pop(0)
#             queue2.append(q)
#             sum_q2+=q
#             sum_q1-=q
#         else:
#             break
#         cnt+=1
#         # if len(queue1)==0 or len(queue2)==0 or cnt>=len(queue1)*3:
#         if cnt>=len(queue1)*3:
#             cnt=-1
#             break
#     return cnt

# def solution(queue1, queue2):
#     answer = -2
#     target = get_target(queue1, queue2)
#     # print(target)
#     answer = proc_comparison(queue1,queue2,target)
#     return answer

#### 다른 사람 코드 사용
from collections import deque

def solution(queue1, queue2):
    answer, max_count = 0, len(queue1) * 3
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    total = s1 + s2

    if s1 == s2:
        return 0
    elif total % 2 == 1:
        return -1
    
    while True:
        if s1 > s2:
            move = q1.popleft()
            q2.append(move)
            s1 -= move
            s2 += move
            answer += 1
        elif s1 < s2:
            move = q2.popleft()
            q1.append(move)
            s1 += move
            s2 -= move
            answer += 1
        else:
            break
        if max_count == answer:
            answer = -1
            break

    return answer
# [출처] [Python] 프로그래머스 - 두 큐 합 같게 만들기, 메뉴 리뉴얼|작성자 코딩의명수