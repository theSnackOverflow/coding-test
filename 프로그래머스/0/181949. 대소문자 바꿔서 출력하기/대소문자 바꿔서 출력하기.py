str = input()

result = ""

for s in str:
    if s.islower():
        new_char = s.upper()
    else:
        new_char = s.lower()
        
    result += new_char
    
print(result)
    
    

