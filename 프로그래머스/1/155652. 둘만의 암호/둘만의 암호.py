def solution(s, skip, index):
    answer = ''
    for c in s:
        cnt=index
        n=ord(c)
        while cnt>0:
            n+=1
            if n>ord('z'):
                n= ord('a')
                
            if chr(n) in skip:
                continue
            cnt-=1
        
        answer+=chr(n)
    return answer