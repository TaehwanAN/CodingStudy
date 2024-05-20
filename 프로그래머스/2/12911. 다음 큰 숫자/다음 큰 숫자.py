def solution(n):
    answer = 0
    # 제한사항이 100만 까지 이므로 재귀함수를 이용해서 n+1을 계속 매개변수로 전달하는 방식 보다는 while문 이용
    # n의 이진수의 1의 개수 확인
    # n에서 부터 while문 따라서 무한히 커지는 수 플래그변수
    # 플래그변수의 이진수의 1의 개수가 같으면 반복문종료하고 플래그변수 리턴
    cntOne=format(n,'b').count('1')
    nFlag=n+1
    while cntOne!=format(nFlag,'b').count('1'):
        nFlag+=1
    answer=nFlag
    return answer