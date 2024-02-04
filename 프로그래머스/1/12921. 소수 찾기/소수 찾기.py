# def prime_num(number):
#     for i in range(2,number):
#         if number%i==0:
#             return False
#     return True

# def solution(n):
#     answer=0
#     for number in range(2,n+1):
#         if prime_num(number):
#             answer+=1
#     return answer

## 시간 초과발생, 위 코드의 시간복잡도=O(N^2)
## gpt 코드: 에라토스테네스의 체 방식
# def sieve_of_eratosthenes(n):
def solution(n):
    # 길이가 n+1인 True만 존재하는 리스트를 만들고, 0과 1은 소수가 아니므로 False로 바꾼다.
    is_prime = [True] * (n + 1) 
    is_prime[0] = is_prime[1] = False
    
    ## 2~n까지를 순회한다.
    # 인덱스에 해당하는 값에 True가 남아있다면, 그 인덱스가 소수인지를 검토한다.
    # 소수에 해당한다면, 그 소수를 약수로 갖는 모든 수를 제거한다.
    # 예를 들어 2를 검토하면 4에서 n까지 2씩 증가하면서 모든 짝수를 False로 바꿔준다.
    # 이후 3을 검토하여 9에서 n까지 3씩 증가시킨다.
    # 4는 False이므로 건너뛴다.
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    ## 남아있는 소수, 즉 True만을 더해준다.
    # 시간복잡도는 O(log log N)이 된다.
    return sum(is_prime)
