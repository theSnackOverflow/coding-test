def solution(before, after):
    before =''.join(sorted(before))
    after = ''.join(sorted(after))
    return  int(before == after)