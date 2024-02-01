def solution(s):
    answer = True
    if not(s.isnumeric()):
        return False
    if not(len(s)==4 or len(s)==6):
        return False
    return answer