def solution(t, p):
    answer = 0
    l=len(p)
    for i in range(0,len(t)-l+1):
        t_part=t[i:i+l]
        if p>=t_part:
            answer+=1
    return answer