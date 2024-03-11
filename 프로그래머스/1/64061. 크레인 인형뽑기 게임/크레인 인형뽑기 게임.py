def solution(board, moves):
    answer = 0
    stack = []  # 스택 초기화

    for m in moves:
        m = m - 1
        for k, v in enumerate(board):
            if v[m] == 0:
                continue
            else:
                if stack and v[m] == stack[-1]:  # 스택이 비어있지 않고, 인형이 같은 경우
                    stack.pop()
                    answer += 2  # 인형 두 개가 사라지므로 2를 더함
                else:
                    stack.append(v[m])
                board[k][m] = 0  # 인형을 뽑았으므로 해당 칸을 0으로 표시
                break

    return answer