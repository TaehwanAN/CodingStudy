# def solution(priorities, location):
#     answer = 0
#     ## 알고리즘 분석
#     # 1. 리스트의 가장 처음을 꺼내온다.
#     # 2. 꺼내온 값 보다 큰 값의 존재를 확인한다.
#     # 2.1 더 큰 값이 존재하는 경우, 꺼내온 값을 다시 리스트의 가장 뒤로 붙인다.
#     ##      + location을 
#     # 2.2 더 큰 값이 존재하지 않는 경우, 실행한다(카운트를 올린다)
#     # 3. 원하는 위치의 값을 확인하는 방법
#     # 3.1 값을 꺼내올때 마다 1씩 줄인다. 
#     # 3.1.1 location아 0이 되었을때 꺼내온 값이 알고 싶은 값이다. 만약 리스트에 더 큰 값이 남아있다면, 리스트에 붙이고 나서 location을 len -1 로 바꿔준다.
#     # 3.1.2 만약 location==0일때의 꺼내온 값 보다 큰 값이 없으면 카운트를 세고서 리턴한다.
    
#     while True:
#         p=priorities.pop(0)
#         location-=1
        
#         if p>=max(priorities):
#             answer+=1
#             if location==-1:
#                 return answer
#         else:
#             priorities.append(p)
#             if location==-1:
#                 location=len(priorities)-1
#         print(priorities)
#     return answer


### 런타임 에러 발생...
# def solution(priorities, location):
#     answer = 0
#     while True:
#         p=priorities.pop(0)
#         location-=1
        
#         if p>=max(priorities):
#             answer+=1
#             if location==-1:
#                 return answer
#         else:
#             priorities.append(p)
#             if location==-1:
#                 location=len(priorities)-1
#         # print(priorities)
#     return len(priorities)


### 인터넷에서 다른 알고리즘 접근법 발견
## 각 원소를 튜플의 형태로 (인덱스, 값)을 queue로 만든다.
## any를 사용하여 조건을 체크한다.

def solution(priorities,location):
    answer=0
    queue=[(i,v) for i,v in enumerate(priorities)]
    while True:
        q=queue.pop(0)
        if any([i for i in queue if i[1]>q[1]]):
            queue.append(q)
            continue
        else:
            answer+=1
        if q[0]==location:
            return answer
    

