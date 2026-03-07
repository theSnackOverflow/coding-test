def solution(myString):
    newString = ''
    for char in myString:
        if char == "a": newString += char.upper()
        elif char == "A": newString += char
        else: newString += char.lower()
    return newString
