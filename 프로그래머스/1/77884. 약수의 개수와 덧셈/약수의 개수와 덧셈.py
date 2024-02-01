def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        divisor_list=[]
        for j in range(1,i+1):
            if i%j==0:
                divisor_list.append(j)
        if len(divisor_list)%2:
            answer-=i
        else: answer+=i
    return answer