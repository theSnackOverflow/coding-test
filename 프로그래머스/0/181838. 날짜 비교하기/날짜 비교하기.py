def solution(date1, date2):
    date1, date2 = list(map(str, date1)), list(map(str, date2))
    date1, date2 = int("".join(date1)), int("".join(date2))
    return int(date1 < date2)