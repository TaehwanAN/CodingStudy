def solution(new_id):
    answer = ''
    id_processing=''
    ## 1단계
    id_processing=new_id.lower()
    
    ## 2단계
    import re
    allowed=re.compile('[\w\d\-\_\.]?')
    id_processing=''.join(re.findall(allowed, id_processing))
    # print(id_processing)
    
    ## 3단계
    find_dots=re.compile('[\.]{2,}')
    id_processing=re.sub(find_dots,'.', id_processing)
    # print(id_processing)
    
    ## 4단계
    id_processing=id_processing.strip('.')
    
    ## 5단계
    if len(id_processing)==0:
        id_processing='a'
        
    ## 6단계
    if len(id_processing)>=16:
        id_processing=id_processing[0:15]
        # print(len(id_processing))
        while True:
            if id_processing[-1]=='.':
                id_processing=id_processing.rstrip('.')
            else:
                break
    
    ## 7단계
    if len(id_processing)<=2:
        while True:
            if len(id_processing)==3:
                break
            else:
                id_processing+=id_processing[-1]
                
    answer= id_processing
    return answer