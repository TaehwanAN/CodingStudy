def solution(n, m):
    answer = []
    n,m=min([n,m]), max([n,m])
    for i in range(n,0,-1):
        if (m%i==0) and (n%i==0):
            answer.append(i)
            break
    l=m
    while True:
        if (l%n==0) and (l%m)==0:
            answer.append(l)
            break
        l+=1
    return answer