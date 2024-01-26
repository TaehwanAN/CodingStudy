## My Original Code
# def solution(number, k):
#     # ## 일단 1개만 없앴을 때 제일 크게 되는 수 구하고, 그 수에서 또 1개만 없앴을 때 제일 크게 되는 수 구하는 방식으로? 이 짓을 k번 반복해보면 될듯?
#     for _ in range(k): # 총 반복횟수: k번
#         m=0 # 변수간 비교에 사용할 플래그 변수
#         for i in range(len(number)): # number를 순회하면서 각 자리를 빼보고 m과 비교해보기
#             if m<int(number[:i]+number[i+1:]): # m보다 크면 m 대체
#                 m=int(number[:i]+number[i+1:])
#         number=str(m)
#     return number

# GPT help: 
# 이 코드는 각 숫자를 검사하면서 스택의 맨 위에 있는 숫자가 현재 숫자보다 작고 아직 제거할 숫자가 남아 있다면 그 숫자를 제거합니다. 
# 이렇게 하면 항상 가장 큰 숫자가 스택의 맨 위에 오게 됩니다. 
# 마지막으로 아직 제거할 숫자가 남아 있다면 스택의 맨 뒤에서부터 제거합니다. 
# 이렇게 하면 k개의 숫자를 제거한 후 남은 가장 큰 숫자를 얻을 수 있습니다. 
# 이 코드는 숫자를 한 번만 순회하므로 시간 복잡도는 O(n)입니다.

def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0: # 2. 이미 있는 숫자 중에 새로 들어갈 숫자보다 작은 수들 k개 지워줌
            k -= 1 
            stack.pop()
        stack.append(num) # 1. 리스트에 숫자 추가
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

    
