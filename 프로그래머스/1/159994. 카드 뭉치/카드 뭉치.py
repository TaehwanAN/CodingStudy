def solution(cards1, cards2, goal):

    for g in goal:
        if g in cards1:
            c1=cards1.pop(0)
            if g!=c1:
                return "No"
        if g in cards2:
            c2=cards2.pop(0)
            if g!=c2:
                return "No"
    return "Yes"