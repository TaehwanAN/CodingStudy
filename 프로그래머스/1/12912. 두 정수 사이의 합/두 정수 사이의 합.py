def solution(a, b):
    answer = 0
    if a==b:
        answer=a
    else:
        a,b=sorted([a,b])
        answer=sum([i for i in range(a,b+1)])
        
    return answer