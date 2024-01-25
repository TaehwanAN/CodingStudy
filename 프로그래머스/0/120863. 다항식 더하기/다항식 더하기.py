def solution(polynomial):
    x_coef = 0
    constant = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            constant+=int(c)
        else:
            x_coef = x_coef+1 if c=='x' else x_coef+int(c[:-1])
    if x_coef == 0:
        return str(constant)
    elif x_coef==1:
        return 'x + '+str(constant) if constant!=0 else 'x'
    else:
        return f'{x_coef}x + {constant}' if constant!=0 else f'{x_coef}x'