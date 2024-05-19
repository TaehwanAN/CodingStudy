def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    A.sort()
    B.sort(reverse=True)
    
    for a,b in zip(A,B):
        answer+= a*b
    
    return answer