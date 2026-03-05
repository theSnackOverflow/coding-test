def solution(n):
    one_dim = []
    for i in range(n):
        for j in range(n):
            if i == j:
                one_dim.append(1)
            else:
                one_dim.append(0)
    two_dim = [one_dim[i:i+n] for i in range(0, len(one_dim), n)]
    return two_dim
