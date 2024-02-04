from itertools import combinations
def prime_num(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    for c in combinations(nums,3):
        if prime_num(sum(c)):
            answer+=1
    

    return answer