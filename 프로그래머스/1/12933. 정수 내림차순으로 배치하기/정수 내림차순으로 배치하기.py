def solution(n):
    l=sorted(list(str(n)), reverse=True)
    answer=int(''.join(l))
    
    return answer