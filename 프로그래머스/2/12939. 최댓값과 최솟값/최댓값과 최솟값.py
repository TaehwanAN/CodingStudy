def solution(s):
    answer =''
    sList=[ int(x) for x in s.split(' ')]
    sList.sort()
    answer=f'{sList[0]} {sList[-1]}'
    return answer