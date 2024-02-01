from itertools import combinations
def solution(number):
    answer = 0
    for tup in combinations(number,3):
        # print(tup)
        if sum(tup)==0:
            answer+=1
    return answer