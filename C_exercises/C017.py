#Faça um programa que leia um número inteiro N e imprima a soma de todos os fatoriais entre 0 e N (inclusive N).
#Não utilize bibliotecas matemáticas.
n = int(input())
soma = 0
while n >= 0:
    fatorial = 1
    i = n
    if n == 0:
        soma += 1
    else:
        while i > 0:
            if i != 0:    
                fatorial = fatorial * i
            i += (-1)
        soma += fatorial
    n += (-1)
print(soma)
