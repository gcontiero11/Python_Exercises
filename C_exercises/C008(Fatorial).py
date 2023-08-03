#O fatorial de um número inteiro positivo N, denotado por N!, é definido como o produto dos inteiros positivos menores ou iguais a N. 
#Por exemplo 4! = 4 × 3 × 2 × 1 = 24.
#Faça um programa que leia um número inteiro N e imprima o seu fatorial. 
#Não utilize bibliotecas matemáticas.
n = int(input())
fatorial = 1
i = n
while i > 0:
    fatorial = fatorial * i
    i = i - 1   
print(fatorial)
