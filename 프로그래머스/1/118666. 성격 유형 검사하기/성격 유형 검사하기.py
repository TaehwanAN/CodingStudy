def solution(survey, choices):
    answer = ''
    ## 알고리즘 분석:
    # 1. 해쉬 구조로 자료 저장한다.
    # 2. choices에 -4 하여, 0을 기준으로 -3~3의 범위가 되도록 한다.
    # 3. choices의 값이 음수인지 양수인지에 따라 survey의 값을 결정해준다.
    # 4. 전체 반복은 zip으로 survey와 choice를 묶는다
    
    p_types=dict() # personality type => dictionary
    personality='RTCFJMAN'
    for p in personality:
        p_types[p]=0
        
    
    choices=[c-4 for c in choices]
    
    
    for p,c in zip(survey,choices):
        if c<0: # choice가 음수라면 survey에서 넘어온 원소의 첫번째 값에 choice 절대값 만큼 +
            p_types[p[0]]+=abs(c)
        elif c>0: 
            p_types[p[1]]+=abs(c)
    def type_decision(s): # RT, CF, JM,AN을 받음
        answer=''
        if p_types[s[0]]>=p_types[s[1]]:
            answer=s[0]
        else:
            answer=s[1]
        return answer
    
    for s in ['RT','CF','JM','AN']:
        answer+=type_decision(s)
    return answer