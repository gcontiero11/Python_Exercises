s = input()
c = input()
aparicao = 0

for i in range(len(s)):
    if s[i] == c:
        aparicao += 1
print(aparicao)        