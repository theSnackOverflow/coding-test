def solution(binomial):
    list = binomial.split()
    op = list[1]
    if op == "+":
        return int(list[0]) + int(list[2])
    elif op == "-":
        return int(list[0]) - int(list[2])
    else:
        return int(list[0]) * int(list[2])
