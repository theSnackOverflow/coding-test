def solution(myString, pat):
    string = ''
    for char in myString:
        if char == "A":
            string += 'B'
        else: string += "A"
    if pat in string:
        return 1
    else: return 0
