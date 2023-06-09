s = input()

palindromo = True

j = len(s)
i = 0
while i < j:
    if s[i] == " ":
        i += 1
    elif s[j - 1] == " ":
        j -= 1    
    else:    
        if s[j - 1] != s[i]:
            palindromo = False
        i += 1
        j -= 1        
if palindromo:
    print(1)
else:
    print(0)    
