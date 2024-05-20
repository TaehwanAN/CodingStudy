def solution(s):
    answer = []
    cntWhile=0
    cntRemoveZero=0
    while s!='1':
        cntWhile+=1
        cntRemoveZero+=s.count('0')
        s=format(len(s.replace('0','')), 'b')
    answer.append(cntWhile)
    answer.append(cntRemoveZero)
    return answer