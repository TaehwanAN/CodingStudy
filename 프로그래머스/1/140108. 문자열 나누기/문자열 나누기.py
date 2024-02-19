def solution(s):
    answer = 0
    count=0
    x=''
    for i,v in enumerate(s):
        if count==0:
            answer+=1
            x=v
        if x==v:
            count+=1
        else:
            count-=1
        
    return answer