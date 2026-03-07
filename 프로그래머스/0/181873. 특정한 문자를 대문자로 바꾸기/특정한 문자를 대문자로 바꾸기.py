def solution(my_string, alp):
    my_string = list(my_string)
    my_string = [char.upper() if alp == char else char for char in my_string ]
    return ("").join(my_string)
        
