def solution(arr):
    answer = 0
    while True:
        answer+=1
        check=True
        for a in arr:
            if answer%a!=0:
                check=False
        if check:
            return answer