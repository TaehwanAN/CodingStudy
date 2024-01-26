def solution(s):
    s=s.lower()
    if ('p' not in s) and ('y' not in s): return True
    return True if s.count('p')==s.count('y') else False

    