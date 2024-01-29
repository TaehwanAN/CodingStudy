def solution(x):
    answer = True
    if x%sum(list(map(int,list(str(x)))))!=0:
        answer=False
        
    return answer