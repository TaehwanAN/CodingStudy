def solution(spell, dic):
    
    for d in dic:
        if all([s in d for s in spell]):
            return 1
    return 2