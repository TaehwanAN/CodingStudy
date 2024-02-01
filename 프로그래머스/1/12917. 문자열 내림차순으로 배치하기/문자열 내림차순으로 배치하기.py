def solution(s):
    answer = ''.join(sorted([c for c in s], reverse=True))
    return answer