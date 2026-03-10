def solution(a, b, c):

    list = [a, b, c]
    list = set(list)
    if len(list) == 3:
        return a + b + c
    elif len(list) == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return 27 * (a) * (a**2) * (a**3)
    
