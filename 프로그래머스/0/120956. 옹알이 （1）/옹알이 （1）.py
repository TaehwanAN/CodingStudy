def solution(babbling):
    answer = 0
    # available=['aya','ye','woo','ma']
    # for b in babbling:
    #     for a in available:
    #         b=b.replace(a,'')
    #     if len(b)==0:
    #         answer+=1

    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:  # babbling의 단어 하나씩 확인
        for c in can:
            if c * 2 not in bab:  # 연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(c, ' ')
                
        if bab.isspace():  # 공백으로만 이루어져 있으면 answer+1
            answer += 1
            

    return answer