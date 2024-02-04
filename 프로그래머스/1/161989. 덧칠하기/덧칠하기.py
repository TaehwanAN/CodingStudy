# def solution(n, m, section):
#     answer = 0
#     all_walls=[True if i not in section else False for i in range(1,n+1)]
    
#     while (not all([b==True for b in all_walls])):
#         for i in range(0,len(all_walls)-m,1):
#             if not (all_walls[i]): # false 라면 i에서 i+m까지 모두 True로 변경
#                 for j in range(i,i+m):
#                     all_walls[j]=True
#         answer+=1
        
#     return answer

# def solution(n, m, section):
#     answer = 0
#     ## 덧칠할 부분: False
#     all_walls=[True if i not in section else False for i in range(1,n+1)]
#     # print(all_walls)
    
#     ## 종료조건: 모든 벽이 칠해져서 True값만 남았을때.
#     while (sum(all_walls)!=n):
#         for i in section:
#             if all_walls[i-1]==False: # false 라면 i에서 i+m까지 모두 True로 변경
#                 for j in range(i-1,i+m-1):
#                     if j<n:
#                         all_walls[j]=True
#                 answer+=1  
#             else:
#                 continue 
#         # print(all_walls)
        
#     return answer



## 시간초과 발생...
## 알고리즘 재고민:
# 일단 section에서 한번에 칠할수 있는 범위의 값은 제외하고, 칠해야하는 부분의 처음 값만 남는 리스트를 만들어서, 이 리스트의 길이를 재면 의외로 쉬울지도.
def solution(n,m,section):
    answer=[section[0]]
    for s in section[1:]:
        if s<(answer[-1]+m):
            continue
        answer.append(s)
        
        
    return len(answer)