# def solution(scoville, K):
#     answer = 0
#     first_food=0
#     second_food=0
#     while True:
#         if min(scoville)>=K:
#             break
#         first_food=scoville.pop(0)
#         second_food=scoville.pop(0)
#         scoville.insert(0,(first_food+2*second_food))
#         answer+=1
#     return answer

# import heapq as hq # heapq 모듈
# def solution(scoville, K):
#     hq.heapify(scoville) # 리스트를 힙큐로 변환
#     answer=0
#     while True:
#         first=hq.heappop(scoville) # heappop: 가장 작은 원소 제거함과 동시에 리턴
#         if first>=K:
#             break # 만약 힙큐의 최소값이 K보다 크면 반복 중단
#         else:
#             second=hq.heappop(scoville)
#             hq.heappush(scoville, (first+second**2)) #heappush: 머리에 아이템 삽입
#             answer+=1
#     return answer if answer>0 else -1
# import heapq as hq
# def solution(scoville,K):
#     answer=0
#     hq.heapify(scoville)
#     while True:
        
#         first=hq.heappop(scoville)
#         if first>=K: break
#         second=hq.heappop(scoville)
#         hq.heappush(scoville, (second*2+first))
#         answer+=1
    
#     return answer if answer>0 else -1
## 이 이상은 무리데스 gpt 찬스
import heapq as hq

def solution(scoville, K):
    answer=0
    hq.heapify(scoville)
    while scoville[0]<K:
        mix=hq.heappop(scoville) + (hq.heappop(scoville)*2)
        hq.heappush(scoville,mix)
        answer+=1
        if len(scoville)==1 and scoville[0]<K:
            return -1
    return answer
## https://docs.python.org/ko/3/library/heapq.html