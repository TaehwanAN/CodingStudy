def solution(a, b):
    ## 1. a와 b를 기약분수로 만들기
    # 1.1. a와 b의 공약수가 있다면 나눠주기
    # 1.2 나눠진 값을 다시 재귀하기
    for i in range(2,a+1):
        if ((a%i==0) and (b%i==0)):
            return solution(a//i,b//i)
    
    ## 2. 소인수 담을 리스트
    prime_list=[]
    
    ## 3. b의 소인수 구하기
    i = 2
    while i <= b:
        if b % i == 0:
            b //= i
            prime_list.append(i)
        else:
            i += 1
    # print(prime_list)
    
    ## 4. 만약 소인수 리스트의 모든 원소가 2나 5에 해당하면 True, 2나 5이외의 소인수가 있다면 False
    if all([p in [2,5] for p in prime_list]):
        return 1
    return 2