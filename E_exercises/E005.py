s1 = input().upper()
s2 = input().upper()

anagrama = True
num_letras_s1 = 0
num_letras_s2 = 0

for i in range(len(s1)):
    letra = s1[i]
    if letra != " ":
        for j in range(len(s1)):
            if letra == s1[j]:
                num_letras_s1 += 1
        for k in range(len(s2)):
            if letra == s2[k]:
                num_letras_s2 += 1
        if num_letras_s1 != num_letras_s2:
            anagrama = False
if anagrama:
    print(1)
else:
    print(0)