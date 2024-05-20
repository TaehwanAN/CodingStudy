def solution(n):
    answer = 1 # 자기자신으로 표현하는 방법 반드시 카운트
    # 플래그 변수 : 연속한 자연수들의 합을 담을 변수
    # 1부터 자기 자신-1 까지 순환
    # 그 수부터 연속한 수들 순환하면서 플래그변수 증가시키기
    ## 만약 플래그 변수가 n 과 같아지면 answer를 1증가하고순환문 종료
    ## 만약 플래그변수가 n 보다 커지면 그냥 순환문 종료
    
    for i in range(1,n):
        sumFlag=0
        for j in range(i,n):
            sumFlag+=j
            if sumFlag==n:
                answer +=1
                break
            elif sumFlag>n:
                break
    
    return answer