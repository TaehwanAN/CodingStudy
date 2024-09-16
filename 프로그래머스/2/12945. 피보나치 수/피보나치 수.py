
def solution(n):
    answer = 0
    first = 1
    second = 1
    for _ in range(n-2):
        answer = first+second
        first = second
        second = answer
        # print(answer)
    return answer%1234567