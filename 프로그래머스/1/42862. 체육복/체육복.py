def solution(n, lost, reserve):
    ## 최종반환값: n-(체육복 없는 사람 수)
    # 1. 빌려줄수 있는사람: 여벌 있는데 누가 쎄려가서 여벌 입어야 해서 못빌려주는 사람 제외
    lender= set(reserve) - set(lost)
    # 2. 빌려야 하는 사람: 누가 쎄려갔는데 여벌을 다행히 챙겨온 인간 제외
    borrower= set(lost) - set(reserve)
    # 3. 만약 빌려야 하는 사람 없으면 그대로 모든 학생 다 수업 참여 가능 -> for 문 첫줄로 합침
    # 4. lender 가 borrower 빌려주면 borrower 리스트에서 지워준다
    for l in lender:
        ### 만약 borrower가 모두 사라지면, borrower가 none이 되어 none iterable error 발생하므로,
        if borrower==None: return n
    # 4.1 일단 앞 번호 인간 빌려줄 수 있으면 먼저 빌려주자
        if l-1 in borrower:
            borrower.remove(l-1)
    # 4.2 앞 번호 못빌려주면 뒷번호 빌려주자.
        elif l+1 in borrower:
            borrower.remove(l+1)
    # 4.3 두 번호 다 없으면 걍 여벌 체육복 잉여됨.
        
    return n-len(borrower)
